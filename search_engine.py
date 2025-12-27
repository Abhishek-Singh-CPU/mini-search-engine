import os
import re
from collections import defaultdict


class MiniSearchEngine:
    def __init__(self, documents_path: str):
        self.documents_path = documents_path
        self.index = defaultdict(set)
        self.documents = {}
        self._build_index()

    def _tokenize(self, text: str):
        """
        Convert text to lowercase words and remove punctuation.
        """
        return re.findall(r"\b[a-zA-Z]+\b", text.lower())

    def _build_index(self):
        """
        Build an inverted index mapping terms to document names.
        """
        for filename in os.listdir(self.documents_path):
            file_path = os.path.join(self.documents_path, filename)

            if not filename.endswith(".txt"):
                continue

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.documents[filename] = content

                words = self._tokenize(content)
                for word in words:
                    self.index[word].add(filename)

    def search(self, query: str):
        """
        Search documents and rank them based on term frequency.
        """
        query_terms = self._tokenize(query)
        scores = defaultdict(int)

        for term in query_terms:
            for doc in self.index.get(term, []):
                scores[doc] += 1

        return sorted(scores.items(), key=lambda x: x[1], reverse=True)
