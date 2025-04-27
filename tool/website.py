import requests


def summarize_website(url: str) -> str:
    """
    Công cụ trả về nội dung của website
    Args:
        url (str): url của website
    Return:
        str: nội dung của trang website
    """
    print("✅ Tool call: summarize_website")
    try:
        response = requests.get("https://r.jina.ai/"+url)
        if response.status_code != 200:
            return f"URL không tồn tại hoặc không thể truy cập"
        return response.text
    except:
        return f"URL không tồn tại hoặc không thể truy cập"
