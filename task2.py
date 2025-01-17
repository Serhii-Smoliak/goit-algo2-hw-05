import time
import json
from datasketch import HyperLogLog


def exact_unique_ips(file_path):
    unique_ips = set()
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                log_entry = json.loads(line)
                unique_ips.add(log_entry["remote_addr"])
            except (json.JSONDecodeError, KeyError):
                continue
    return len(unique_ips)


def hyperloglog_unique_ips(file_path, precision=14):
    hll = HyperLogLog(precision)
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                log_entry = json.loads(line)
                hll.update(log_entry["remote_addr"].encode("utf-8"))
            except (json.JSONDecodeError, KeyError):
                continue
    return hll.count()


if __name__ == "__main__":
    log_file = "lms-stage-access.log"

    start_time = time.time()
    exact_count = exact_unique_ips(log_file)
    exact_time = time.time() - start_time

    start_time = time.time()
    approx_count = hyperloglog_unique_ips(log_file)
    approx_time = time.time() - start_time

    print("\nРезультати порівняння:")
    print(f"{'':<30}{'Точний підрахунок':<20}{'HyperLogLog':<20}")
    print(f"{'Унікальні елементи':<30}{exact_count:<20}{approx_count:<20}")
    print(f"{'Час виконання (сек.)':<30}{exact_time:<20.5f}{approx_time:<20.5f}")
