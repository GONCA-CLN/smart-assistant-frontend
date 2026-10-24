Streamlit ile chatbot arayüzü geliştirme
    sanal ortam oluşturma:
        python -m venv venv
        .\venv\Scripts\activate
    kurulumlar:
        pip install streamlit requests

    Backend URL: https://smart-assistant-backend-ziz7.onrender.com

    streamlit run app.py

Frontend uygulamasını docker ile test et
    requirements.txt
    Dockerfile

    Image oluşturmak için:
    docker build -t smart-assistant-frontend .

    Docker i ayağa kaldırmak için:
    docker run -d -p 8501:8501 --name smart-assistant-frontend-container smart-assistant-frontend

    http://localhost:8501

Frontendin Github'a yüklenmesi ve Streamlit Cloud'da yayınlama
    .gitignore

    git init
    git add .
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/GONCA-CLN/smart-assistant-frontend.git
    git push -u origin main