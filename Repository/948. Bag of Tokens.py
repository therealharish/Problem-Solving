class Solution:
	def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
		tokens.sort()
		left = 0
		right = len(tokens) - 1
		score = 0
		maxScore = 0
		if (tokens and min(tokens) > power):
			return 0
		while (left <= right):
			if (power >= tokens[left]):
				power -= tokens[left]
				score += 1
				maxScore = max(maxScore, score)
				left += 1
			elif (power < tokens[left]):
				power += tokens[right]
				score -= 1
				right -= 1
		return maxScore
