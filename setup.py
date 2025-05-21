from setuptools import setup, find_packages

setup(
    name="langchain-teddynote",
    version="0.3.45",
    description="LangChain Helper Library",
    author="Teddy Lee",
    author_email="teddylee777@gmail.com",
    url="https://github.com/teddylee777/langchain-teddynote",
    install_requires=[
        "langchain",
        "langgraph",
        "kiwipiepy",
        "rank_bm25",
        "pinecone-client[grpc]",
        "pinecone-text",
        "olefile",
        "pdf2image",
        "openai",
        "anthropic",
        "deepl",
        "feedparser",
        "tavily-python",
        "pandas",
    ],
    packages=find_packages(exclude=[]),
    keywords=[
        "langchain",
        "langgraph",
        "teddynote",
    ],
    python_requires=">=3.10",
    package_data={},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
