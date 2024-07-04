import re
import keyboard

# Initialize the context and responses
context = {}
unrecognized_count = 0  # Counter for unrecognized inputs

responses = {
    'aspirenex': "AspireNex is a platform for internships, jobs, and online training. How can I assist you with AspireNex?",
    'apply.*internship': "You can apply for internships by creating an account on AspireNex, browsing available internships, and submitting your application directly through the platform. Do you need help with any specific internship?",
    'internships.*available': "AspireNex offers a variety of internships in different fields such as engineering, management, media, and more. Are you interested in any particular field?",
    'fee.*register': "No, registration on AspireNex is free. Would you like to know how to get started?",
    'create.*account': "To create an account on AspireNex, visit the website and click on the 'Register' button. Fill in your details and follow the instructions. Do you need assistance with the registration process?",
    'benefits.*internship': "Internships provide hands-on experience, help build professional networks, and enhance your resume. Are you looking to apply for an internship soon?",
    'stipend.*internship': "Yes, many internships on AspireNex offer a stipend. The stipend amount varies depending on the internship. Would you like more information on a specific internship?",
    'jobs.*available': "AspireNex offers a variety of job opportunities in different fields such as engineering, management, media, and more. Are you looking for a job in a particular field?",
    'apply.*job': "You can apply for jobs by creating an account on AspireNex, browsing available jobs, and submitting your application directly through the platform. Do you need help with the job application process?",
    'fee.*apply.*jobs': "No, applying for jobs on AspireNex is free. Would you like to know how to find job listings?",
    'create.*job account': "To create an account for job applications on AspireNex, visit the website and click on the 'Register' button. Fill in your details and follow the instructions. Do you need guidance on creating your profile?",
    'benefits.*job': "Jobs provide long-term employment, help build a career, and offer financial stability. Are you currently searching for job opportunities?",
    'salary.*jobs': "The salary for jobs on AspireNex varies depending on the position and the company. Would you like to know more about salaries in a specific industry?",
    'help|assist': "Sure, I'm here to help! You can ask me about internships, job applications, registration processes, and more. What do you need assistance with?",
    'how to get started': "To get started on AspireNex, create an account, complete your profile, and start browsing internships or job opportunities that match your interests. Do you need help with the first step?",
    'profile': "A complete profile includes your resume, skills, experience, and a professional photo. This helps employers and internship providers know more about you. Do you need tips on building a strong profile?",
    'contact support': "You can contact AspireNex support through the 'Contact Us' page on the website. They are available to help with any issues or questions you may have. Do you need the link to the support page?",
    'training programs': "AspireNex offers various online training programs to help you develop new skills. Are you interested in any specific training program or field?",
    'feedback': "We value your feedback! You can submit your feedback through the feedback form on the AspireNex website. Would you like me to guide you on where to find it?",
    'thank you|thanks': "You're welcome! I'm glad I could help. If you have any more questions, feel free to ask."
}

def chatbot_response(user_input):
    global context, unrecognized_count
    user_input = user_input.lower()

    if 'follow_up' in context:
        follow_up = context.pop('follow_up')

        follow_up_responses = {
            'internship_help': {
                'yes': "Great! Please specify which internship you need help with.",
                'no': "Alright, let me know if you have any other questions."
            },
            'get_started': {
                'yes': "To get started on AspireNex, create an account by visiting the website and clicking on the 'Register' button.",
                'no': "Okay, feel free to ask me anything else you need help with."
            },
            'registration_help': {
                'yes': "To create an account, visit the AspireNex website, click on 'Register', fill in your details, and follow the instructions.",
                'no': "Alright, let me know if you need help with anything else."
            },
            'profile_help': {
                'yes': "Make sure to include your resume, skills, experience, and a professional photo in your profile.",
                'no': "Okay, feel free to ask me anything else you need help with."
            },
            'specific_internship': {
                'yes': "Please provide the details of the internship you're interested in.",
                'no': "Alright, let me know if there's something else I can assist with."
            }
        }

        if re.search(r'\byes\b', user_input):
            return follow_up_responses[follow_up]['yes']
        elif re.search(r'\bno\b', user_input):
            return follow_up_responses[follow_up]['no']
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            unrecognized_count = 0
            if 'internship' in pattern:
                context['follow_up'] = 'internship_help'
            if 'get started' in pattern:
                context['follow_up'] = 'get_started'
            if 'registration' in pattern:
                context['follow_up'] = 'registration_help'
            if 'profile' in pattern:
                context['follow_up'] = 'profile_help'
            if 'internship' in pattern:
                context['follow_up'] = 'specific_internship'
            return response

    unrecognized_count += 1
    if unrecognized_count >= 3:
        unrecognized_count = 0
        return "We are connecting you to a live agent from our branch. Hold for a minute."
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase your question or ask about something specific related to AspireNex?"

def main():
    print("Hello! I am AspireNexBot. How can I help you today?")
    while True:
        try:
            if keyboard.is_pressed('esc'):
                print("Goodbye!")
                break
            user_input = input("You: ")
            response = chatbot_response(user_input)
            print(f"AspireNexBot: {response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
