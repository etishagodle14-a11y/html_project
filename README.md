# HTMLMaker — Visual HTML Code Generator 🛠️

A Django-powered web tool that lets users visually build HTML structures and instantly copy the generated code — no deep coding knowledge required.

---

## The Problem It Solves

Beginners and non-developers often struggle to write HTML structure from scratch. Opening a blank file and typing tags manually is intimidating and error-prone.

**HTMLMaker removes that barrier** — users build their HTML structure through a clean visual interface, and the tool generates ready-to-use code that can be copied in one click.

---

## Features

- **Visual HTML Builder** — Build HTML structures through an intuitive interface without writing code manually
- **One-Click Copy to Clipboard** — Instantly copy generated HTML code for use in any project
- **Clean Matte UI** — Soft, eye-friendly design using Bootstrap — comfortable for long sessions
- **Beginner Friendly** — Designed so users with minimal coding knowledge can build real HTML structures
- **Dynamic UI Updates** — JavaScript handles live changes so the output updates as you build
- **Responsive Design** — Works across desktop and mobile browsers

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Database | PostgreSQL |
| Scripting | JavaScript |

---

## Screenshots

> _Add screenshots here — the builder interface, generated code panel, and copy button in action._
> _Create a `/screenshots` folder and use:_
> `![Builder UI](screenshots/builder.png)`
> `![Code Output](screenshots/output.png)`

---

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/etishagod/html-maker.git
cd html-maker

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up PostgreSQL database
# Create a database named 'htmlmaker_db' in PostgreSQL
# Update DB credentials in settings.py:
# NAME: htmlmaker_db
# USER: your_postgres_user
# PASSWORD: your_password

# 5. Apply migrations
python manage.py migrate

# 6. Run the development server
python manage.py runserver
```

Open your browser at `http://127.0.0.1:8000`

---

## Project Structure

```
html-maker/
├── manage.py
├── requirements.txt
├── htmlmaker/                  # Project settings
│   ├── settings.py
│   └── urls.py
└── generator/                  # Main app
    ├── models.py               # Saved configurations / user data
    ├── views.py                # Builder logic, code generation
    ├── urls.py
    └── templates/
        ├── index.html          # Main builder interface
        └── output.html         # Generated code display
    └── static/
        ├── css/
        │   └── style.css       # Matte, soft UI custom styles
        └── js/
            └── builder.js      # Dynamic UI + copy to clipboard logic
```

---

## How the Copy to Clipboard Works

```javascript
// builder.js

function copyToClipboard() {
    const code = document.getElementById('generated-code').innerText;
    navigator.clipboard.writeText(code).then(() => {
        const btn = document.getElementById('copy-btn');
        btn.innerText = 'Copied!';
        setTimeout(() => btn.innerText = 'Copy to Clipboard', 2000);
    });
}
```

> The Clipboard API is used for a smooth, modern copy experience — the button text changes to "Copied!" for 2 seconds as visual feedback, then resets automatically.

---

## UI Design Philosophy

HTMLMaker uses a **soft matte design system** — avoiding harsh whites and bright contrasts that cause eye strain during extended use.

Key design decisions:
- Muted background tones instead of pure `#ffffff` white
- Subtle border radius on all components for a friendly feel
- Bootstrap utility classes for consistent spacing and responsiveness
- High contrast only where it matters — the generated code panel and action buttons

---

## What I Learned

- Building a tool-based Django application (not just CRUD)
- Using JavaScript alongside Django Templates for dynamic, real-time UI
- Implementing the Clipboard API for smooth UX interactions
- Designing with user comfort in mind — matte, accessible color choices
- Connecting Django to PostgreSQL for storing user configurations

---

## Future Improvements

- [ ] Add user accounts to save and revisit generated HTML structures
- [ ] Export generated code as a downloadable `.html` file
- [ ] Add CSS and Bootstrap class selector to the builder
- [ ] Build a REST API version using Django REST Framework
- [ ] Deploy live on Railway or Render
- [ ] Add syntax highlighting to the code output panel (using Prism.js)
- [ ] Dark mode toggle

---

## Author

**Etisha Godle**
- GitHub: [@etishagod](https://github.com/etishagod)
- LinkedIn: [Etisha Godle](https://www.linkedin.com/in/etisha-godle-636744275)
- Email: etishagodle14@gmail.com

---

> Built with Django, Python, Bootstrap & JavaScript | Designed for developers and beginners alike
