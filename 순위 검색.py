import pandas as pd

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
info_df = pd.DataFrame(
    [
        {
            'lang': row[0],
            'job': row[1],
            'career': row[2],
            'soul_food': row[3],
            'score': row[4]}
        for row in list(map(lambda x: x.split(), info))
    ]
)
info_df['score'] = info_df['score'].astype(int)

answer = []
for i in query:
    lang, _, job, _, career, _, soul_food, score = i.split()
    query_str = ""
    if lang != '-': query_str += f"(lang == '{lang}') and"
    if job != '-': query_str += f"(job == '{job}') and"
    if career != '-': query_str += f"(career == '{career}') and"
    if soul_food != '-': query_str += f"(soul_food == '{soul_food}') and"
    if score != '-': query_str += f"(score >= {score})"
    answer.append(len(info_df.query(query_str)))
print(answer)

info_df.loc[info_df.lang == 'java']