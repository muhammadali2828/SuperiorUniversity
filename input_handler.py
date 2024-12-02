from transformers import pipeline

gen = pipeline('text-generation', model='gpt2')

def create_objective(skills, degree):
    txt = f"Generate a career objective for a {degree} student with the following skills: {', '.join(skills)}"
    obj = gen(txt, max_length=50, num_return_sequences=1)[0]['generated_text']
    return obj.strip()

def get_input():
    print("--------------Welcome to the AI-powered CV generator -----------\n")
    user_data = {}
    user_data['Name'] = input("Enter your full name: ")
    user_data['Contact'] = input("Enter your contact number: ")
    user_data['Address'] = input("Enter your address: ")
    
    skills = input("\nList your skills (comma separated): ").split(',')
    degree = input("Enter your degree (e.g., BS in Computer Science): ")
    user_data['Objective'] = create_objective(skills, degree)
    
    user_data['Education'] = []
    while True:
        degree_info = input("Enter your Education details (leave blank to stop):\nDegree (e.g., BS Computer Science): ")
        if not degree_info:
            break
        institution = input("Institution name: ")
        year = input("Year of Completion: ")
        user_data['Education'].append({'degree': degree_info, 'institution': institution, 'year': year})

    user_data['Experience'] = []
    while True:
        job_title = input("Enter your job title (leave blank to stop): ")
        if not job_title:
            break
        company = input("Company name: ")
        year_start = input("Start year: ")
        year_end = input("End year: ")
        user_data['Experience'].append({'job_title': job_title, 'company': company, 'year_start': year_start, 'year_end': year_end})

    user_data['Skills'] = input("Enter your key skills (comma separated): ").split(',')

    return user_data
