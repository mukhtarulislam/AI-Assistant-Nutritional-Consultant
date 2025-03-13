from fpdf import FPDF

def generate_pdf(text, output_filename="diet_plan.pdf"):
    # Convert to string if necessary
    # if not isinstance(text, str):
    #     try:
    #         text= text.result
    #         # text = str(text)
    #     except AttributeError:
    #         text=str(text)        # except Exception as e:
    #         # raise ValueError("Unable to extract text from crewoutput object") from e
    # Directly convert CrewOutput to string using its native output
    if hasattr(text, 'output'):
        text = text.output
    elif hasattr(text, 'result'):
        text = text.result

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Split text into lines and add them to the PDF
    lines = text.split('\n')
    for line in lines:
        pdf.multi_cell(0, 10, line)
    
    pdf.output(output_filename)
    return output_filename
