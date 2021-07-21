from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

def scrap_text(url,disease_name):
    html_text=requests.get(url).text
    arr=[]
    disease=[]
    soup = BeautifulSoup(html_text,'lxml')
    tags = soup.find_all('div',id="content_qna-toc")
    for tag in tags:
        ptags=tag.find_all('p')
        for atags in ptags:
            if(atags.text!='Overview' and atags.text!='DDX' and atags.text!='Treatment' and atags.text!='Guidelines' and atags.text!='Medications' and atags.text!='Workup' and atags.text!='Presentation'):
                arr.append(atags.text)
                disease.append(disease_name)
            
    arr=pd.DataFrame(arr)
    disease=pd.DataFrame(disease)
    final_df=pd.concat([arr,disease],axis=1)
    return final_df


allergic_rhintis=scrap_text('https://emedicine.medscape.com/article/134825-questions-and-answers','allergic rhintis')
food_alergies=scrap_text('https://emedicine.medscape.com/article/135959-questions-and-answers','food alergies')
conjuctivitus=scrap_text('https://emedicine.medscape.com/article/1191467-questions-and-answers','conjunctivitis')
anaphylaxis=scrap_text('https://emedicine.medscape.com/article/135065-questions-and-answers','anaphylaxis')
ard_syndrome=scrap_text('https://emedicine.medscape.com/article/165139-questions-and-answers','ard syndrome')
pediatric_sinusitris=scrap_text('https://emedicine.medscape.com/article/873149-questions-and-answers','pediatric sinisitrius')
merged_df=pd.concat([allergic_rhintis,food_alergies,conjuctivitus,anaphylaxis,ard_syndrome,pediatric_sinusitris])
merged_df.to_csv('allergy_data.csv')



