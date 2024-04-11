# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> path: tokenB->tokenA->tokenC->tokenE->tokenD->tokenC->tokenB <br/>
> (1) tokenB->tokenA : amountIn:5.0, amountOut:5.655 <br/>
> (2) tokenA->tokenC : amountIn:5.655, amountOut:2.372 <br/>
> (3) tokenC->tokenE : amountIn:2.372, amountOut:1.530 <br/>
> (4) tokenE->tokenD : amountIn:1.530, amountOut:3.451 <br/>
> (5) tokenD->tokenC : amountIn:3.451, amountOut:6.685 <br/>
> (6) tokenC->tokenB : amountIn:6.685, amountOut:22.497 <br/>
> tokenB balance=22.49722180697414

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> 因為 AMM 的價格是由流動池中不同資產的數量來決定，因此在執行交易時交易價格可能受到其他交易者影響，而期望交換到的貨幣數量和實際交換的貨幣數量之間的差異就稱為 slippage。 <br/>
> 在 Uniswap V2 中，可設置交易的最小接收量，使交易如果超過預期 slippage 則不執行，來預防 slippage。 <br/>
> 像是 swapExactTokensForTokens 的五個參數分別是 amountIn, amountOutMin, path, to, deadline，其中 amountIn 是輸入的貨幣數量，而 amountOutMin 就是最小能接受的貨幣數量，如果目前能換出的貨幣數量 < amountOutMin 則交易不執行。

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> 在 initial liquidity minting 時，會從 LP token 減掉一個 minimum liquidity。這個設計是防止早期的 liquidity provider 能投入少量的貨幣就操控整個流動池的價格，造成未來投資者回報遠小於早期投資者，影響流動池長期發展，因此用 minimum liquidity 來增加公平性，並鼓勵更多 liquidity provider 參與。

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> liquidity = Math.min(amount0.mul(_totalSupply) / _reserve0, amount1.mul(_totalSupply) / _reserve1); <br/>
> 這個公式是為了確保每個時間加入的 liquidity provider 都能獲得公平的比例，讓投入流動池的貨幣能兌換到相對應的 LP token。用 min 函數也讓 liquidity provider 需要投入相同價值的兩種貨幣。


## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Sandwich Attack 是在發現有利可圖的交易時，在這筆交易前安插自己的交易並賺取利差。像是發現有人要購買貨幣前，用較低的價格買入再用較高的價格賣給他。若在 initiating a swap 時成為 sandwich attack 的目標，可能會使 slippage 增加，讓我們以更高的價格買入或更低的價格賣出，造成交易損失。
