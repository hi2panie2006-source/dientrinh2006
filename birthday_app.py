import streamlit as st
import base64
import os

# Cấu hình trang web
st.set_page_config(
    page_title="Thiệp Sinh Nhật Bất Ngờ 🎂", 
    page_icon="🎁", 
    layout="centered"
)

# --- THANH CÀI ĐẶT ---
with st.sidebar:
    st.header("⚙️ Tùy Chỉnh Thiệp")
    recipient_name = st.text_input("👤 Tên người nhận:", value="Vũ Phạm Kiều Duyên")
    sender_name = st.text_input("✍️ Người gửi:", value="E của chị")
    
    wishes_content = st.text_area(
        "💌 Lời chúc mừng:", 
        value="Chúc mừng sinh nhật chị nha, chúc chị tuổi mới mau ăn chóng lớn, gặp nhiều may mắn, cầu tiền được tiền cầu tài được tài, sớm ngày đạt được ước mơ của mình! 🎂💖<br><br>"
              "Chúc mừng sinh nhật chị nha, chúc chị tuổi mới mau ăn chóng lớn, gặp nhiều may mắn, cầu tiền được tiền cầu tài được tài, sớm ngày đặt được ước mơ của mình. Happy birthday chị 🎂 💖 😜<br><br>"
              "<b>P/s:</b> Sớm ngày lên chiến thần nhé chị, à mà chị vẫn nhớ là sau này lấy chồng giàu thì bao nuôi thằng e nhé 😏 😋 🎂🎉"
    )
    youtube_url = st.text_input("🎵 Link nhạc YouTube phát nền:", value="https://www.youtube.com/watch?v=hhGVTTMjM8o")

# --- TỰ ĐỘNG QUÉT VÀ NẠP TẤT CẢ ẢNH CÓ TRONG THƯ MỤC ---
supported_extensions = (".jpg", ".jpeg", ".png")
images_base64 = []

# Lấy tất cả file ảnh có trong thư mục hiện tại của file code
current_dir = os.getcwd()
for file in sorted(os.listdir(current_dir)):
    if file.lower().endswith(supported_extensions):
        file_path = os.path.join(current_dir, file)
        try:
            with open(file_path, "rb") as img_file:
                b64_str = base64.b64encode(img_file.read()).decode("utf-8")
                images_base64.append(b64_str)
        except:
            pass

slides_html = ""
if images_base64:
    slides_items = ""
    for idx, b64 in enumerate(images_base64):
        active_class = "active" if idx == 0 else ""
        slides_items += """
            <div class="mySlides {}">
                <img src="data:image/jpeg;base64,{}" style="width: 100%; height: 220px; object-fit: cover; border-radius: 15px;" />
            </div>
        """.format(active_class, b64)
    slides_html = """
        <div class="slideshow-container">
            {}
            <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
            <a class="next" onclick="plusSlides(1)">&#10095;</a>
        </div>
        <div style="text-align:center; margin-bottom: 10px;">
            <span class="dot" onclick="currentSlide(1)"></span> 
            <span class="dot" onclick="currentSlide(2)"></span> 
        </div>
    """.format(slides_items)
else:
    slides_html = "<p style='color: #ffeb3b; font-size: 13px;'>⚠️ Chưa tìm thấy file ảnh nào trong thư mục! Hãy chép ảnh vào chung thư mục với file code.</p>"

# Trích xuất Video ID từ link YouTube
try:
    if "watch?v=" in youtube_url:
        video_id = youtube_url.split("watch?v=")[1].split("&")[0]
    elif "youtu.be/" in youtube_url:
        video_id = youtube_url.split("youtu.be/")[1].split("?")[0]
    else:
        video_id = "hhGVTTMjM8o"
except:
    video_id = "hhGVTTMjM8o"

# --- GIAO DIỆN WEB THIỆP CHÍNH ---
html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1f1c2c 0%, #928dab 100%);
            color: #ffffff;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow-x: hidden;
        }}
        .container {{
            width: 90%;
            max-width: 500px;
            text-align: center;
            padding: 20px;
        }}
        .card {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(12px);
            border: 2px solid rgba(255, 255, 255, 0.2);
            border-radius: 25px;
            padding: 25px 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        
        /* SLIDESHOW ẢNH KỶ NIỆM */
        .slideshow-container {{
            position: relative;
            margin-bottom: 10px;
        }}
        .mySlides {{ display: none; }}
        .mySlides.active {{ display: block; }}
        .prev, .next {{
            cursor: pointer;
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            padding: 8px;
            color: white;
            font-weight: bold;
            font-size: 16px;
            background-color: rgba(0,0,0,0.4);
            border-radius: 50%;
            user-select: none;
            transition: 0.3s;
        }}
        .prev {{ left: 5px; }}
        .next {{ right: 5px; }}
        .prev:hover, .next:hover {{ background-color: rgba(0,0,0,0.8); }}

        /* MINIGAME BÓNG BAY */
        .balloon-grid {{
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 25px 0;
            flex-wrap: wrap;
        }}
        .balloon {{
            font-size: 55px;
            cursor: pointer;
            transition: transform 0.2s;
            user-select: none;
            animation: float 2s infinite ease-in-out alternate;
        }}
        .balloon:hover {{ transform: scale(1.2); }}
        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            100% {{ transform: translateY(-12px); }}
        }}

        /* BÁNH KEM BÍ MẬT */
        .cake-box {{
            cursor: pointer;
            transition: transform 0.3s;
            display: inline-block;
            margin: 20px 0;
        }}
        .cake-box:hover {{ transform: scale(1.1); }}
        .cake-icon {{ font-size: 80px; }}
        .secret-text {{
            color: #ffeb3b;
            font-size: 18px;
            font-weight: bold;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
            animation: pulse 1.5s infinite;
        }}
        @keyframes pulse {{
            0% {{ opacity: 0.6; }}
            50% {{ opacity: 1; }}
            100% {{ opacity: 0.6; }}
        }}

        #game-section {{ display: block; }}
        #cake-section {{ display: none; }}
        #card-section {{ display: none; animation: fadeIn 1.5s forwards; }}
        #yt-player {{ width: 0; height: 0; border: none; position: absolute; visibility: hidden; }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .title-h1 {{ color: #ff758c; font-size: 28px; font-weight: bold; margin-bottom: 5px; }}
        .name-h2 {{ color: #ffeb3b; font-size: 24px; font-weight: bold; margin-bottom: 10px; }}
        .wishes {{ font-size: 14px; line-height: 1.5; font-style: italic; color: #f1f1f1; text-align: left; background: rgba(0,0,0,0.2); padding: 12px; border-radius: 12px; max-height: 180px; overflow-y: auto; }}
        .sender {{ margin-top: 15px; font-weight: bold; color: #a7ffeb; font-size: 14px; }}

        /* BẢNG ĐIỀU KHIỂN NHẠC NỔI */
        .music-control-panel {{
            position: fixed;
            top: 15px;
            right: 15px;
            background: rgba(30, 30, 46, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 8px 12px;
            border-radius: 15px;
            display: none;
            z-index: 999;
            box-shadow: 0 4px 15px rgba(0,0,0,0.4);
            backdrop-filter: blur(8px);
            text-align: left;
        }}
        .music-control-panel button {{
            background: rgba(255, 255, 255, 0.2);
            border: none;
            color: white;
            padding: 5px 10px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 12px;
            font-weight: bold;
            width: 100%;
            margin-bottom: 5px;
        }}
        .music-control-panel button:hover {{ background: rgba(255, 255, 255, 0.4); }}
        .music-control-panel label {{ font-size: 11px; color: #ddd; display: block; margin-top: 3px; }}
        .music-control-panel input[type=range] {{ width: 100%; cursor: pointer; }}
    </style>
</head>
<body>

    <!-- BẢNG ĐIỀU KHIỂN NHẠC -->
    <div id="musicPanel" class="music-control-panel">
        <button id="musicBtn" onclick="toggleMusic()">🔊 Tắt Nhạc</button>
        <label>Âm lượng: <span id="volVal">100</span>%</label>
        <input type="range" id="volRange" min="0" max="100" value="100" oninput="changeVolume(this.value)">
    </div>

    <div class="container">
        <!-- BƯỚC 1: MINIGAME BÓNG BAY -->
        <div id="game-section" class="card">
            <h2 style="color: #ff758c; margin-bottom: 10px;">🎈 BẤM BÓNG MỞ QUÀ 🎈</h2>
            <p style="font-size: 14px; color: #ddd;">Làm nổ hết 3 quả bóng bay để xuất hiện món quà bất ngờ!</p>
            
            <div class="balloon-grid">
                <span class="balloon" id="b1" onclick="popBalloon('b1')">🎈</span>
                <span class="balloon" id="b2" onclick="popBalloon('b2')">🎈</span>
                <span class="balloon" id="b3" onclick="popBalloon('b3')">🎈</span>
            </div>
            <p id="game-status" style="font-size: 16px; font-weight: bold; color: #ffeb3b;">Còn lại 3 quả bóng...</p>
        </div>

        <!-- BƯỚC 2: BÁNH KEM BÍ MẬT -->
        <div id="cake-section" class="card">
            <h2 style="color: #ff758c; margin-bottom: 5px;">🎉 XUẤT HIỆN QUÀ TẶNG! 🎉</h2>
            <div class="cake-box" onclick="openSecretCard()">
                <div class="cake-icon">🎂</div>
                <div class="secret-text">👉 Chạm vào đây để mở bí mật! 👈</div>
            </div>
        </div>

        <!-- BƯỚC 3: THIỆP CHÚC MỪNG -->
        <div id="card-section" class="card">
            {slides_html}
            <div class="title-h1">🎂 HAPPY BIRTHDAY! 🎂</div>
            <div class="name-h2">✨ {recipient_name} ✨</div>
            <hr style="border: 1px solid rgba(255,255,255,0.2); margin: 10px 0;">
            <div class="wishes">"{wishes_content}"</div>
            <div class="sender">— Gửi từ: {sender_name} —</div>
        </div>
    </div>

    <div id="yt-player"></div>

    <script>
        let slideIndex = 1;
        showSlides(slideIndex);

        function plusSlides(n) {{
            showSlides(slideIndex += n);
        }}

        function currentSlide(n) {{
            showSlides(slideIndex = n);
        }}

        function showSlides(n) {{
            let i;
            let slides = document.getElementsByClassName("mySlides");
            if (slides.length === 0) return;
            if (n > slides.length) {{ slideIndex = 1 }}
            if (n < 1) {{ slideIndex = slides.length }}
            for (i = 0; i < slides.length; i++) {{
                slides[i].style.display = "none";
                slides[i].className = slides[i].className.replace(" active", "");
            }}
            slides[slideIndex-1].style.display = "block";
            slides[slideIndex-1].className += " active";
        }}

        let popped = 0;
        let isPlaying = true;
        let player;

        var tag = document.createElement('script');
        tag.src = "https://www.youtube.com/iframe_api";
        var firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

        function onYouTubeIframeAPIReady() {{
            player = new YT.Player('yt-player', {{
                height: '0',
                width: '0',
                videoId: '{video_id}',
                playerVars: {{
                    'autoplay': 0,
                    'controls': 0,
                    'loop': 1,
                    'playlist': '{video_id}'
                }},
                events: {{
                    'onReady': function(event) {{
                        event.target.setVolume(100);
                    }}
                }}
            }});
        }}

        function popBalloon(id) {{
            let b = document.getElementById(id);
            if (b.innerText !== "💥") {{
                b.innerText = "💥";
                b.style.animation = "none";
                popped++;
                let remaining = 3 - popped;
                
                if (remaining > 0) {{
                    document.getElementById("game-status").innerText = "Còn lại " + remaining + " quả bóng...";
                }} else {{
                    setTimeout(() => {{
                        document.getElementById("game-section").style.display = "none";
                        document.getElementById("cake-section").style.display = "block";
                    }}, 500);
                }}
            }}
        }}

        function openSecretCard() {{
            document.getElementById("cake-section").style.display = "none";
            document.getElementById("card-section").style.display = "block";
            document.getElementById("musicPanel").style.display = "block";

            if (player && typeof player.playVideo === 'function') {{
                player.playVideo();
            }}
        }}

        function toggleMusic() {{
            let btn = document.getElementById("musicBtn");
            if (isPlaying) {{
                if (player && typeof player.pauseVideo === 'function') {{ player.pauseVideo(); }}
                btn.innerText = "🔇 Bật Nhạc";
                isPlaying = false;
            }} else {{
                if (player && typeof player.playVideo === 'function') {{ player.playVideo(); }}
                btn.innerText = "🔊 Tắt Nhạc";
                isPlaying = true;
            }}
        }}

        function changeVolume(val) {{
            document.getElementById("volVal").innerText = val;
            if (player && typeof player.setVolume === 'function') {{
                player.setVolume(parseInt(val));
            }}
        }}
    </script>
</body>
</html>
"""

html_code = html_template.format(
    slides_html=slides_html,
    recipient_name=recipient_name,
    wishes_content=wishes_content,
    sender_name=sender_name,
    video_id=video_id
)

st.components.v1.html(html_code, height=720)