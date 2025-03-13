import gradio as gr
from pipeline import run_nutrition_advisor
from pdf_generator import generate_pdf

def generate_plan(age, gender, height, weight, activity_level, goals,
                  medical_conditions, medications, allergies,
                  food_preferences, cooking_ability, budget, cultural_factors):
    # Prepare user information dictionary
    user_info = {
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "activity_level": activity_level,
        "goals": goals,
        "medical_conditions": medical_conditions if medical_conditions.strip() != "" else "None reported",
        "medications": medications if medications.strip() != "" else "None reported",
        "allergies": allergies if allergies.strip() != "" else "None reported",
        "food_preferences": food_preferences if food_preferences.strip() != "" else "No specific preferences",
        "cooking_ability": cooking_ability,
        "budget": budget,
        "cultural_factors": cultural_factors if cultural_factors.strip() != "" else "No specific factors"
    }
    
    # Run the pipeline to generate the nutrition plan
    result = run_nutrition_advisor(user_info)

    
    if result is None:
        return "An error occurred while generating the nutrition plan.", None
    # print("DEBUG: CrewOutput attributes:", result.__dict__)
    
    # convert the result to a string befor returning.
    try:
        #if the crewoutput has a result attribute use that
        result_text= result.raw
    except AttributeError:
        result_text=str(result)
    # Generate a PDF from the result
    pdf_file = generate_pdf(result, "diet_plan.pdf")
    return result, pdf_file

def create_gradio_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# 🍎🥦🥗🍇🍊🍉🍽️🥕 AI-Assistant Nutritional Consultant")
        gr.Markdown("Get a detailed nutrition plan based on your demographics, health conditions, and preferences.")
        
        with gr.Tab("Basic Information"):
            with gr.Row():
                age = gr.Number(label="Age", value=30)
                gender = gr.Dropdown(choices=["Male", "Female", "Non-binary/Other"], label="Gender", value="Male")
            with gr.Row():
                height = gr.Textbox(label="Height (e.g., 5'10\" or 178 cm)", value="5'10\"")
                weight = gr.Textbox(label="Weight (e.g., 160 lbs or 73 kg)", value="160 lbs")
            activity_level = gr.Dropdown(
                choices=["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extremely Active"],
                label="Activity Level", value="Moderately Active"
            )
            goals = gr.Textbox(label="Nutrition Goals (comma separated)", placeholder="Weight Loss, Muscle Building, etc.")
        
        with gr.Tab("Health Details"):
            medical_conditions = gr.Textbox(label="Medical Conditions (comma separated)", placeholder="Diabetes, Hypertension, etc.")
            medications = gr.Textbox(label="Current Medications (comma separated)", placeholder="Medication1, Medication2")
            allergies = gr.Textbox(label="Food Allergies/Intolerances (comma separated)", placeholder="Gluten, Dairy")
        
        with gr.Tab("Preferences & Lifestyle"):
            food_preferences = gr.Textbox(label="Food Preferences & Dislikes", placeholder="Prefer plant-based, dislike seafood")
            cooking_ability = gr.Dropdown(
                choices=["Very Limited", "Basic/Quick Meals", "Average", "Advanced/Can Spend Time", "Professional Level"],
                label="Cooking Skills & Available Time", value="Average"
            )
            budget = gr.Dropdown(
                choices=["Very Limited", "Budget Conscious", "Moderate", "Flexible", "No Constraints"],
                label="Budget Considerations", value="Moderate"
            )
            cultural_factors = gr.Textbox(label="Cultural or Religious Dietary Factors", placeholder="Halal, Kosher, etc.")
        
        output_text = gr.Markdown(label="Your Personalized Nutrition Plan")
        output_pdf = gr.File(label="Download Nutrition Plan PDF")
        generate_button = gr.Button("Generate Nutrition Plan")
        
        generate_button.click(
            generate_plan,
            inputs=[age, gender, height, weight, activity_level, goals,
                    medical_conditions, medications, allergies,
                    food_preferences, cooking_ability, budget, cultural_factors],
            outputs=[output_text, output_pdf]
        )
        
    return demo

if __name__ == "__main__":
    demo = create_gradio_interface()
    demo.launch()
