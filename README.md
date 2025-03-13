# AI-Assistant Nutritional Consultant

**AI-Assistant Nutritional Consultant** is an AI-powered nutrition planning tool that leverages CrewAI and Gradio to generate a detailed, personalized diet plan based on your demographics, health details, and food preferences. The tool also allows you to download the generated plan as a PDF—all from an intuitive Gradio interface.

## Features

- **AI-Driven Diet Planning:** Uses multiple AI agents to research nutrition, analyze health conditions, and craft custom diet plans.
- **Interactive Gradio Interface:** Enter your personal, health, and dietary information easily through an intuitive UI.
- **PDF Generation:** Automatically convert your personalized nutrition plan into a downloadable PDF.


## Project Structure

AI-Assistant Nutritional Consultant/ ├── AI-Assistant Nutritional Consultant/ 
                                                                  ├── init.py │ 
                                                                  ├── agents.py # Defines the nutrition, medical, and diet planning agents. │ 
                                                                  ├── tasks.py # Sets up tasks for each agent based on user inputs. │ 
                                                                  ├── pipeline.py # Orchestrates the entire CrewAI pipeline. │ 
                                                                  ├── pdf_generator.py # Converts the nutrition plan text into a PDF. 
                                                                  │── main.py # Gradio interface and entry point for the application. 
                                                                  ├── LICENSE 
                                                                  ├── README.md 
                                                                  ├── requirements.txt # List of package dependencies. 
                   



## Prerequisites

- **Python 3.7+**  
- API Keys for OpenAI and SERPER. Create a `.env` file in the project root with your credentials:

  ```env
  SERPER_API_KEY=your_serper_api_key
  OPENAI_API_KEY=your_openai_api_key



## Installation Instructions
- **Step 1: Clone the Repository**
- Clone the repository to your local machine:

git clone https://github.com/your-username/AI-Assistant-Nutritional-Consultant.git
cd AI-Assistant-Nutritional-Consultant
Step 2: Set Up a Virtual Environment (Optional but Recommended)
It is recommended to set up a virtual environment to manage your dependencies. To do this, run the following commands:


python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
Step 3: Install Dependencies
Install the required dependencies by running:

bash
Copy
pip install -r requirements.txt
Step 4: Add Your API Keys
Create a .env file in the project root directory and add your API keys (as shown in the Prerequisites section).

Step 5: Launch the Gradio Interface
Run the following command to start the Gradio interface:

bash
Copy
python nutrition_advisor/main.py
This will launch the web interface where you can enter your personal, health, and dietary information to generate a personalized nutrition plan.

Usage
Open the Gradio interface in your browser (it should automatically open, but you can access it at http://localhost:7860).
Fill in your details:
Demographics (age, gender, etc.)
Health information (existing conditions, allergies, etc.)
Dietary preferences (vegetarian, gluten-free, etc.)
The AI will generate a personalized nutrition plan based on your inputs.
Once the plan is generated, you can download it as a PDF.


License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
If you have any questions or need assistance, feel free to reach out:

Email: Mukhtarulislam88@hotmail.com
GitHub: AI-Assistant Nutritional Consultant
