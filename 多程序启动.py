from multiprocessing import Process, freeze_support
import os

# ==== 配置参数 ====
TOTAL_PAGES = 100     # 要抓的总页数
CHUNK_SIZE = 10      # 每个子进程抓取多少页
START_PAGE = 1        # 起始页码

# ==== 启动函数 ====
def run_scraper(start_page, num_pages):
    print(f"🚀 启动抓取任务：第 {start_page} 页起，抓取 {num_pages} 页")
    os.system(f"test4.py {start_page} {num_pages}")

# ==== 主程序 ====
if __name__ == "__main__":
    freeze_support()  # Windows 必须加！
    processes = []

    for i in range(START_PAGE, START_PAGE + TOTAL_PAGES, CHUNK_SIZE):
        chunk_start = i
        chunk_size = min(CHUNK_SIZE, START_PAGE + TOTAL_PAGES - i)
        p = Process(target=run_scraper, args=(chunk_start, chunk_size))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("✅ 所有子任务完成！已抓取全部页段。")