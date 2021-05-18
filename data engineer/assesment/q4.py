import pandas as pd

path = 'C:/Users/Rizal/Desktop/case_study/pulsify/pulsifi-data-eng-assessment/data engineer/dataset/'
df = pd.read_csv(path + '20210506.csv')

def filter_candidate(df):
    # company id is 5 and has a total of 6 questionnaires
    df = df.loc[(df.company_id == 5) & (df.total_questionnaires == 6)]

    # candidates whom have completed all assessments
    df =  df.loc[(df.total_questionnaires_completed == df.total_questionnaires)]

    # candidates whom met the criteria
    df = df.loc[(df.is_met_criteria == True)]

    print(df.to_string())

def main():
    recommended_candidate = filter_candidate(df)

if __name__ == "__main__":
    main()