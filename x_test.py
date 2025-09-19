import yt_dlp
import csv

# YouTubeチャンネルURL
channel_url = "https://www.youtube.com/@dozle/videos"

# 取得件数
max_downloads = 5

# 出力CSV
output_file = "dozle_videos.csv"

# yt-dlp オプション
ydl_opts = {
    "ignoreerrors": True,       # エラー動画を無視
    "quiet": True,              # 出力を最小化
    "extract_flat": True,       # 動画ページの情報のみ取得
    "skip_download": True,
    "max_downloads": max_downloads
}

videos = []

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(channel_url, download=False)
    entries = info_dict.get("entries", [])
    print(f"取得中: {len(entries)} 件")
    
    for e in entries:
        if e is None:
            continue
        upload_date = e.get("upload_date", "")
        title = e.get("title", "")
        video_id = e.get("id", "")
        url = f"https://youtu.be/{video_id}"
        videos.append([upload_date, title, url])

# CSV書き込み
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["公開日", "タイトル", "URL"])
    writer.writerows(videos)

print(f"CSVファイル '{output_file}' が作成されました。")
