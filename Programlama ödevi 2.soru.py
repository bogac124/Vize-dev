import pandas as pd

data = {
    "Xi": [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65],
    "C1": [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    "C2": [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    "Distance1": [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    "Distance2": [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    "Nearest Cluster": [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    "New Centroid": [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
}

C1 = 16
C2 = 22
print("                                           C1:", C1)
print("                                           C2:", C2)

j = 0
while j < 4:
    a_count = 0
    b_count = 0
    
    i = 0
    while i < len(data["Xi"]):
        data["C1"][i] = C1
        data["C2"][i] = C2
        data["Distance1"][i] = abs(data["Xi"][i] - C1)
        data["Distance2"][i] = abs(data["Xi"][i] - C2)
        
        if data["Distance2"][i] >= data["Distance1"][i]:
            data["Nearest Cluster"][i] = 1
            data["New Centroid"][i] = C1
            a_count += 1
        else:
            data["Nearest Cluster"][i] = 2
            data["New Centroid"][i] = C2
            b_count += 1
        
        i += 1
    
    C1 = sum(data["Xi"][i] for i in range(len(data["Xi"])) if data["Nearest Cluster"][i] == 1) / a_count
    C2 = sum(data["Xi"][i] for i in range(len(data["Xi"])) if data["Nearest Cluster"][i] == 2) / b_count
    
    print(f"Iteration {j+1}:")
    print(pd.DataFrame(data))
    print("                                           C1:", C1)
    print("                                           C2:", C2)
    
    j += 1







