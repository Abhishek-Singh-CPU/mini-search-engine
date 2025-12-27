from flask import Flask, render_template, request
from search_engine import MiniSearchEngine

app = Flask(__name__)

# Initialize search engine once at startup
engine = MiniSearchEngine("documents")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query", "").strip()

    if not query:
        return render_template(
            "index.html",
            error="Please enter a search query."
        )

    results = engine.search(query)

    return render_template(
        "results.html",
        query=query,
        results=results
    )


if __name__ == "__main__":
    app.run(debug=True)
