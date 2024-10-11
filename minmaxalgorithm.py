import math
def min_max(curDepth, nodeIndex,maxTurn, scores, targetDepth):
    if curDepth == targetDepth:
        return scores[nodeIndex]
    if maxTurn:
        return max(min_max(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),min_max(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        return min(min_max(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),min_max(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))
scores = [2,5,6,7,1,-1,0,8]
print(min_max(0, 0, True, scores, 3))
