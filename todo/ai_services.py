import importlib

settings = importlib.import_module("django.conf").settings

openai = importlib.import_module("openai")

class TaskAIService:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY
    
    def categorize_task(self, title, description):
        """Categorize a task using AI"""
        prompt = f"""
        Categorize this task into one of these categories: work, personal, health, shopping, learning, other
        Task: {title}
        Description: {description}
        Return only the category name.
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10
        )
        
        return response.choices[0].message.content.strip().lower()
    
    def suggest_priority(self, title, description, due_date=None):
        """Suggest task priority based on content and context"""
        prompt = f"""
        Analyze this task and suggest priority: high, medium, low
        Consider urgency, importance, and due date.
        Task: {title}
        Description: {description}
        Due Date: {due_date or 'No due date'}
        Return only: high, medium, or low
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=5
        )
        
        return response.choices[0].message.content.strip().lower()