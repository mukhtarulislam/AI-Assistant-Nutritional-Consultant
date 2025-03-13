# setup.py
from setuptools import setup, find_packages

setup(
    name="AI-Assistant Nutritional Consultant",
    version="0.1.0",
    description="A personalized AI-Assistant Nutritional Consultant with a Gradio UI and PDF export.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Mukhtar ul Islam",
    author_email="Mukhtarulislam88@hotmail.com",
    packages=find_packages(),
    install_requires=[
        "crewai",
        "langchain_openai",
        "crewai[tools]",
        "gradio",
        "fpdf",
        "langchain_community",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "uv=AI_Assistant_Nutritional_Consultant.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
