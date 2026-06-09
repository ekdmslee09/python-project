# 1. 데이터 입력
def student_data():
    students = []

    while True:
        # 학생 점수 입력
        score = input("학생 점수를 입력하세요 (0~100, 종료: q): ")

        # q 를 입력하면 종료
        if score.lower() == 'q':
            break

        try:
            # 점수를 float으로
            score = float(score)

            # 점수 범위를 벗어났을 때 다시 입력받기
            if score < 0 or score > 100:
                print("[오류] 점수 범위를 벗어났습니다.")
                continue 
            
            # 리스트에 추가
            students.append(score)

        except ValueError:
            # 숫자가 아닌 값이 입력되었을 때 다시 입력받기
            print("[오류] 숫자가 아닌 값이 입력되었습니다.")

    return students

# 2. 기초 통계량 계산 및 출력
def statistics(students):

    # 리스트에 입력된 점수가 없을 때
    if len(students) == 0:
        print("입력된 점수가 없습니다.")

        return None

    # 점수 리스트를 오름차순으로 정렬
    scores = sorted(students)
    n = len(scores)
    
    # 기초 통계량 계산

    # 평균
    avg = sum(scores) / n 

    # 중앙값
    if n % 2 != 0:
        median = scores[n//2]
    else:
        median = (scores[n//2-1] + scores[n//2]) / 2

    # 제 1, 3 사분위수, IQR
    q1 = scores[n//4]
    q3 = scores[3*n//4]
    iqr = q3 - q1
    
    # 출력
    print("\n--- 기초 통계량 ---")
    print(f"평균: {avg}")
    print(f"중앙값: {median}")
    print(f"최소: {scores[0]}, 최대: {scores[-1]}")
    print(f"Q1: {q1}, Q3: {q3}, IQR: {iqr}")
    
    # 박스플롯을 위해 딕셔너리 반환
    return {"min": scores[0], "q1": q1, "med": median, "q3": q3, "max": scores[-1], "iqr": iqr}


# 3. 히스토그램 출력
def histogram(students):
    print("\n--- 히스토그램 (Histogram) ---")

    counts = []

    # 점수 데이터를 5개 구간으로 나누기 위한 기준점
    for i in range(0, 100, 20):
        # 해당 구간에 속하는 학생 수 세기
        count = 0
        for s in students:
            if i == 80:          # 80~99 이 아닌 80~100
                if i <= s <= 100:
                    count += 1
            else:                # 0~19, 20~39, 40~59, 60~79
                if i <= s < i + 20:
                    count += 1
        
        # 리스트에 추가
        counts.append(count)
        
    # 가장 높은 높이 찾기 
    max_height = 0
    for c in counts:
        if c > max_height:
            max_height = c

    # 출력
    for h in range(max_height,0,-1):
        line = f"{h:2} |"  # 명 수
        for c in counts:
            if c >= h:            # h 높이에 도달하면 [*], 아니면 공백
                line += "  [*]  "
            else:
                line += "       "
        print(line)

    print("    +" + "-" * (len(counts) * 7))
    print("      0-19  20-39  40-59  60-79  80-100")


# 4. 박스플롯 출력
def boxplot(stats):
    print("\n--- 박스플롯 (Boxplot)---")

    scale = 50  # 0~100을 50칸으로 표현
    line = [" "] * (scale + 1) # 공백이 51칸

    # 위치 계산
    min_pos = int(stats["min"] / 100 * scale)
    q1_pos = int(stats["q1"] / 100 * scale)
    med_pos = int(stats["med"] / 100 * scale)
    q3_pos = int(stats["q3"] / 100 * scale)
    max_pos = int(stats["max"] / 100 * scale)


    # 주요 구간 표시
    for i in range(min_pos + 1 , q1_pos):
        line[i] = "-"

    for i in range(q1_pos + 1, q3_pos):
        line[i] = "="

    for i in range(q3_pos + 1 , max_pos):
        line[i] = "-"

    # 주요 지점 표시
    line[min_pos] = "|"
    line[q1_pos] = "["
    line[med_pos] = "|"
    line[q3_pos] = "]"
    line[max_pos] = "|"

    # 출력
    print(f"Min={stats['min']}  Q1={stats['q1']}  Med={stats['med']}  Q3={stats['q3']}  Max={stats['max']}")
    
    print("".join(line)) # 리스트의 원소인 문자열들을 하나의 문자열로 변환
    print("0         20        40        60        80       100")