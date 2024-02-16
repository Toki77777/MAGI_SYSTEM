def majority_vote(results):
    counts = {result: results.count(result) for result in results}
    return max(counts, key=counts.get)

# 例
results = [-1, 500, -1]
majority_result = majority_vote(results)
print("多数派の結果は:", majority_result)
