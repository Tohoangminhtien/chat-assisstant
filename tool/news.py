import requests


def get_news_lastest() -> str:
    """
    Công cụ trả về tin tức mới nhất tại Báo Thanh Niên

    Return:
        str: nội dung của trang web
    """
    print("✅ Tool call: get_news_lastest")
    try:
        response = requests.get("https://r.jina.ai/https://thanhnien.vn/")
        if response.status_code != 200:
            return f"URL không tồn tại hoặc không thể truy cập"
        return response.text
    except:
        return f"URL không tồn tại hoặc không thể truy cập"
