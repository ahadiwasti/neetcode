func maxProfit(prices []int) int {
left, right := 0,1
maxP := 0
for right < len(prices){
    if prices[right] > prices[left]{
          res := prices[right] - prices[left]
            if res > maxP{
                maxP = res
            }
    }else{
        left = right
    }
    right+=1
}
return maxP
}
