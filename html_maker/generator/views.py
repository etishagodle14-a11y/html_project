from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        # 1. DOWNLOAD LOGIC
        if 'download' in request.POST:
            code_to_download = request.POST.get('user_content', '')
            response = HttpResponse(code_to_download, content_type='text/html')
            response['Content-Disposition'] = 'attachment; filename="my_code.html"'
            return response

        user_input = request.POST.get('user_content', '').lower()
        generated_element = ""

        # --- SMART LOGIC FLOW ---

        # 1. WILDLIFE & NATURE
        if any(word in user_input for word in ["wildlife", "animal", "jaanwar", "tiger", "forest"]):
            generated_element = """
            <div style="background: url('https://images.unsplash.com/photo-1546182990-dffeafbe841d?auto=format&fit=crop&w=800&q=60'); background-size: cover; color: white; padding: 60px 20px; border-radius: 15px; text-shadow: 2px 2px 4px #000;">
                <h1>🦁 Wildlife Exploration</h1>
                <p>Experience the majesty of the animal kingdom.</p>
                <button style="padding: 12px 25px; background: #f1c40f; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">Start Safari</button>
            </div>"""

        # 2. EDUCATION & NOTES
        elif any(word in user_input for word in ["education", "notes", "padhai", "study", "kitab"]):
            generated_element = """
            <div style="text-align: left; background: #fffbe6; padding: 25px; border-left: 10px solid #f1c40f; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <h2 style="color: #856404;">📚 Quick Study Notes</h2>
                <ul style="line-height: 1.8; color: #555;">
                    <li><b>Topic:</b> Python Django Framework</li>
                    <li><b>MVT:</b> Model View Template architecture.</li>
                    <li><b>URL Routing:</b> Maps URLs to views.</li>
                </ul>
            </div>"""

        # 3. PRICING TABLE
        elif any(word in user_input for word in ["price", "pricing", "plan", "paise"]):
            generated_element = """
            <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
                <div style="border: 1px solid #ddd; padding: 20px; border-radius: 10px; width: 200px; background: #fff;">
                    <h4>Basic</h4><h2 style="color: #3498db;">$10<span style="font-size: 14px;">/mo</span></h2>
                    <ul style="list-style: none; padding: 0; font-size: 13px; color: #666;"><li>✅ 5 Projects</li><li>✅ Basic Support</li></ul>
                    <button style="background: #3498db; color: white; border: none; padding: 10px; width: 100%; border-radius: 5px;">Buy Now</button>
                </div>
                <div style="border: 2px solid #e74c3c; padding: 20px; border-radius: 10px; width: 200px; background: #fff; transform: scale(1.05);">
                    <small style="color: #e74c3c; font-weight: bold;">POPULAR</small><h4>Premium</h4><h2 style="color: #e74c3c;">$29<span style="font-size: 14px;">/mo</span></h2>
                    <ul style="list-style: none; padding: 0; font-size: 13px; color: #666;"><li>✅ Unlimited Projects</li><li>✅ 24/7 Support</li></ul>
                    <button style="background: #e74c3c; color: white; border: none; padding: 10px; width: 100%; border-radius: 5px;">Buy Now</button>
                </div>
            </div>"""

        # 4. CHART / GRAPH
        elif any(word in user_input for word in ["chart", "graph", "चार्ट", "ग्राफ"]):
            generated_element = """
            <div style="padding: 20px; border: 1px solid #ddd; border-radius: 10px; background: #fff;">
                <h3 style="color: #333;">📈 Data Analytics Report</h3>
                <div style="display: flex; align-items: flex-end; justify-content: space-around; height: 150px; background: #f4f4f4; padding: 10px; border-bottom: 2px solid #333;">
                    <div style="width: 40px; height: 60%; background: #3498db;"></div>
                    <div style="width: 40px; height: 85%; background: #e74c3c;"></div>
                    <div style="width: 40px; height: 45%; background: #2ecc71;"></div>
                    <div style="width: 40px; height: 95%; background: #f1c40f;"></div>
                </div>
            </div>"""

        # 5. IMAGE GALLERY
        elif any(word in user_input for word in ["gallery", "portfolio", "photo", "images"]):
            generated_element = """
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; padding: 10px;">
                <div style="height: 150px; border-radius: 8px; background: url('https://picsum.photos/200/300?random=1'); background-size: cover;"></div>
                <div style="height: 150px; border-radius: 8px; background: url('https://picsum.photos/200/300?random=2'); background-size: cover;"></div>
                <div style="height: 150px; border-radius: 8px; background: url('https://picsum.photos/200/300?random=3'); background-size: cover;"></div>
                <div style="height: 150px; border-radius: 8px; background: url('https://picsum.photos/200/300?random=4'); background-size: cover;"></div>
            </div>"""

        # 6. FAQ SECTION
        elif any(word in user_input for word in ["faq", "sawal", "questions"]):
            generated_element = """
            <div style="max-width: 600px; margin: auto; text-align: left; background: #fff; padding: 20px; border-radius: 10px; border: 1px solid #eee;">
                <h3 style="text-align: center;">Frequently Asked Questions</h3>
                <details style="padding: 10px; border-bottom: 1px solid #eee; cursor: pointer;"><summary style="font-weight: bold;">How to use Magic Box?</summary><p>Just type your command and click generate!</p></details>
                <details style="padding: 10px; border-bottom: 1px solid #eee; cursor: pointer;"><summary style="font-weight: bold;">Is it free?</summary><p>Yes, it's absolutely free for everyone.</p></details>
            </div>"""

        # 7. NEWSLETTER
        elif any(word in user_input for word in ["newsletter", "subscribe", "email list"]):
            generated_element = """
            <div style="background: #6c5ce7; color: white; padding: 40px; border-radius: 15px; text-align: center;">
                <h2>Subscribe to Newsletter 📩</h2>
                <p>Stay updated with our latest magic tricks!</p>
                <input type="email" placeholder="Enter Email" style="padding: 10px; border-radius: 5px; border: none; width: 220px;">
                <button style="padding: 10px 20px; background: #2d3436; color: white; border: none; border-radius: 5px; cursor: pointer;">Join Now</button>
            </div>"""

        # 8. LOGIN FORM
        elif any(word in user_input for word in ["form", "login", "signup", "लॉगिन"]):
            generated_element = """
            <div style="max-width: 300px; margin: auto; padding: 25px; border: 1px solid #eee; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); background: #fff;">
                <h2 style="color: #333;">Sign In</h2>
                <input type="text" placeholder="Username" style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ddd;">
                <input type="password" placeholder="Password" style="width: 100%; padding: 10px; margin-bottom: 15px; border-radius: 5px; border: 1px solid #ddd;">
                <button style="width: 100%; padding: 10px; background: #007bff; color: white; border: none; border-radius: 5px;">Login</button>
            </div>"""

        # 9. TEAM SECTION
        elif any(word in user_input for word in ["team", "members", "log"]):
            generated_element = """
            <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
                <div style="text-align: center;"><div style="width: 80px; height: 80px; background: #3498db; border-radius: 50%; margin: auto; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">JD</div><h4>CEO</h4></div>
                <div style="text-align: center;"><div style="width: 80px; height: 80px; background: #2ecc71; border-radius: 50%; margin: auto; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">AK</div><h4>Developer</h4></div>
            </div>"""

        # 10. MUSIC PLAYER
        elif any(word in user_input for word in ["music", "gaana", "audio", "player"]):
            generated_element = """
            <div style="background: #111; color: white; padding: 20px; border-radius: 50px; display: flex; align-items: center; gap: 20px; width: fit-content; margin: auto;">
                <div style="width: 40px; height: 40px; background: #1db954; border-radius: 50%; display: flex; align-items: center; justify-content: center;">▶</div>
                <span>Now Playing: Lo-fi Beats</span>
            </div>"""

        # 11. BUTTONS
        elif any(word in user_input for word in ["button", "बटन"]):
            color = "#007bff"
            if "lal" in user_input or "red" in user_input: color = "#e74c3c"
            elif "hara" in user_input or "green" in user_input: color = "#2ecc71"
            generated_element = f'<button style="background: {color}; color: white; padding: 12px 25px; border: none; border-radius: 8px; cursor: pointer;">Click Me!</button>'

        # 12. TABLE
        elif any(word in user_input for word in ["table", "टेबल", "data"]):
            generated_element = """
            <table style="width: 100%; border-collapse: collapse; margin-top: 10px; background: #fff;">
                <tr style="background: #333; color: white;"><th>ID</th><th>Name</th><th>Status</th></tr>
                <tr><td style="border: 1px solid #ddd; padding: 8px;">1</td><td style="border: 1px solid #ddd; padding: 8px;">Rahul</td><td style="border: 1px solid #ddd; padding: 8px;">Active</td></tr>
            </table>"""

        # FALLBACK (IF NOTHING MATCHES)
        else:
            generated_element = f"""
            <div style="padding: 30px; border: 2px dashed #f44336; border-radius: 10px; background: #ffebee;">
                <h3 style="color: #f44336;">⚠️ Command Not Recognized</h3>
                <p>Command "<b>{user_input}</b>" samajh nahi aayi. <br>Try: <b>FAQ, Pricing, Education, Wildlife</b></p>
            </div>"""

        # FINAL HTML OUTPUT
        html_code = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: 'Segoe UI', sans-serif; text-align: center; padding: 40px; background-color: #f9f9f9; }}
        * {{ box-sizing: border-box; }}
    </style>
</head>
<body>
    {generated_element}
</body>
</html>"""

        return render(request, 'generator/result.html', {'final_code': html_code, 'user_query': user_input})

    return render(request, 'generator/index.html')