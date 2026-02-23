from flask import Flask, render_template_string, request

app = Flask(__name__)

# English comments strictly
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Legend: Aharon Raanan</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Custom animations */
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-16px); }
            100% { transform: translateY(0px); }
        }
        @keyframes glow {
            0% { text-shadow: 0 0 10px #22c55e, 0 0 20px #22c55e; }
            50% { text-shadow: 0 0 18px #a3e635, 0 0 36px #a3e635; }
            100% { text-shadow: 0 0 10px #22c55e, 0 0 20px #22c55e; }
        }
        .animate-float { animation: float 6s ease-in-out infinite; }
        .animate-glow { animation: glow 3s ease-in-out infinite; }
        .glass-panel {
            background: rgba(15, 23, 42, 0.72);
            backdrop-filter: blur(10px);
        }
    </style>
</head>
<body class="bg-slate-950 text-white font-sans min-h-screen flex flex-col items-center justify-center overflow-hidden relative">

    <!-- Background blobs -->
    <div class="absolute top-0 left-0 w-full h-full overflow-hidden -z-10">
        <div class="absolute top-[-10%] left-[-10%] w-96 h-96 bg-emerald-600 rounded-full mix-blend-multiply filter blur-3xl opacity-20"></div>
        <div class="absolute top-[-10%] right-[-10%] w-96 h-96 bg-lime-500 rounded-full mix-blend-multiply filter blur-3xl opacity-15"></div>
        <div class="absolute bottom-[-20%] left-[20%] w-96 h-96 bg-cyan-600 rounded-full mix-blend-multiply filter blur-3xl opacity-15"></div>
    </div>

    <div class="glass-panel text-center p-10 rounded-3xl shadow-2xl border border-slate-700 max-w-3xl w-[92%] transform hover:scale-[1.02] transition duration-500">

        <h1 class="text-6xl md:text-7xl font-black text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 via-lime-400 to-cyan-400 mb-2 animate-glow">
            AHARON RAANAN
        </h1>

        <p class="text-lg md:text-2xl text-emerald-200 mb-8 font-light tracking-widest uppercase">
            Systems Builder • CS Student • Git & Docker Enjoyer
        </p>

        <!-- Profile cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-5 text-left mb-8">
            <div class="bg-slate-800/40 p-4 rounded-xl border border-slate-700 hover:border-emerald-400 transition">
                <h3 class="text-xl font-bold text-emerald-300 mb-2">💻 Full-Stack Projects</h3>
                <p class="text-slate-300 text-sm">
                    Builds real systems: DB projects, GUIs, layered architectures, and clean code.
                </p>
            </div>
            <div class="bg-slate-800/40 p-4 rounded-xl border border-slate-700 hover:border-lime-400 transition">
                <h3 class="text-xl font-bold text-lime-300 mb-2">🐧 UNIX & DevOps Path</h3>
                <p class="text-slate-300 text-sm">
                    Growing in Linux, Bash, Docker, and modern engineering workflows.
                </p>
            </div>
            <div class="bg-slate-800/40 p-4 rounded-xl border border-slate-700 hover:border-cyan-400 transition">
                <h3 class="text-xl font-bold text-cyan-300 mb-2">🧠 Algorithmic Mind</h3>
                <p class="text-slate-300 text-sm">
                    Loves OS, compilers, algorithms, and the “why” behind performance.
                </p>
            </div>
            <div class="bg-slate-800/40 p-4 rounded-xl border border-slate-700 hover:border-fuchsia-400 transition">
                <h3 class="text-xl font-bold text-fuchsia-300 mb-2">🚀 Ship Mentality</h3>
                <p class="text-slate-300 text-sm">
                    “If it runs in Docker, it runs anywhere.” That’s the rule.
                </p>
            </div>
        </div>

        <!-- Name input -> Hello -->
        <div class="bg-slate-900/50 border border-slate-700 rounded-2xl p-5 text-left">
            <h2 class="text-2xl font-bold mb-3">Say Hello 👋</h2>

            <form method="POST" action="/hello" class="flex flex-col md:flex-row gap-3">
                <input
                    class="w-full md:flex-1 px-4 py-3 rounded-xl bg-slate-950 border border-slate-700 focus:outline-none focus:ring-2 focus:ring-emerald-400"
                    type="text"
                    name="name"
                    placeholder="Type your name..."
                    required
                />
                <button
                    class="px-6 py-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 font-bold transition"
                    type="submit"
                >
                    Submit
                </button>
            </form>

            {% if message %}
            <div class="mt-4 p-4 rounded-xl bg-slate-950 border border-emerald-700 text-emerald-200">
                {{ message }}
            </div>
            {% else %}
            <p class="mt-3 text-slate-400 text-sm">You will get: Hello &lt;name&gt;.</p>
            {% endif %}
        </div>

        <!-- Extra buttons -->
        <div class="flex flex-col md:flex-row justify-center gap-4 mt-8">
            <a href="/aharon" class="px-8 py-3 rounded-full bg-slate-700 hover:bg-slate-600 font-bold transition">
                /aharon
            </a>
            <a href="/raanan" class="px-8 py-3 rounded-full bg-slate-700 hover:bg-slate-600 font-bold transition">
                /raanan
            </a>
        </div>
    </div>

    <footer class="absolute bottom-4 text-slate-600 text-xs">
        Powered by Flask • Styled by Tailwind CDN
    </footer>
</body>
</html>
"""

@app.get("/")
def index():
    # Render page without message initially
    return render_template_string(HTML_CONTENT, message=None)

@app.post("/hello")
def hello():
    # Receive the user's name from the form
    name = (request.form.get("name") or "").strip()
    if not name:
        return render_template_string(HTML_CONTENT, message="Please provide a name.")
    return render_template_string(HTML_CONTENT, message=f"Hello {name}!")

# Your original endpoints, adapted to your name
@app.get("/aharon")
def aharon():
    return "Hello Aharon!"

@app.get("/raanan")
def raanan():
    return "Hello Aharon Raanan!"

if __name__ == "__main__":
    # Use 0.0.0.0 for Docker / external access
    app.run(host="0.0.0.0", port=8000, debug=False)