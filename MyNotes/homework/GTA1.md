# 博弈论第一次作业

### Question 1

**Solve:** 
令$c=\frac{a_1}{2} $.
已知$S_{n+1}\geq 2S_n$,则$S_{n+1}-S_n\geq S_n$,即$a_{n+1}\geq S_n$.
利用数学归纳法,有:
当n=1时,$a_1\geq 2\times \frac{a_1}{2} =a_1$成立
假设当$n=k$时,有:
$a_k\geq 2^k\frac{a_1}{2} =2^{k-1}a_1$
成立,那么当$n=k+1$时,有:
$a_{k+1}\geq S_k=\sum_{i=1}^{k}a_i\geq \sum_{i=1}^{k}2^{i-1}a_1=(2^k-1)a_1\geq (2^{k+1}-2)\frac{a_1}{2} $.
由于当$k>1$时,$2^{k+1}-2> 2^k$,所以原式成立,得证.

### Question 2

**Solve**
因为$v=(1,1,-1)$是矩阵
$$
A=\left[
\begin{matrix}
2 & -1 & b \\\
5 & a & 3  \\\
-1 & 2 & -1 \
\end{matrix}
\right]
$$
的特征向量,所以有:$Av=\lambda v$,那么:
$$
Av=\left[
\begin{matrix}
2 & -1 & b \\\
5 & a & 3  \\\
-1 & 2 & -1 \
\end{matrix}
\right](1,1,-1)^T=(-b+1,a+2,2)^T \\
\therefore \lambda v=(\lambda,\lambda,-\lambda)^T=(-b+1,a+2,2)^T
\\\therefore\lambda=-2,a=-4,b=3
$$

## Question 3

**Solve**

要证明$for\  \epsilon \in [0,1], \frac{1}{2}(1+\sqrt{1+4\epsilon^2})e^{1-\sqrt{1-4\epsilon^2}}\leq e^{-(\epsilon^2-\epsilon^3)/2}$,即要求:
$f(\epsilon)=\frac{1}{2}(1+\sqrt{1+4\epsilon^2})e^{1-\sqrt{1-4\epsilon^2}}-e^{-(\epsilon^2-\epsilon^3)/2}\leq 0 \ \forall \epsilon \in [0,1]$恒成立.
同取对数,即:
$g(\epsilon)=\ln(1+\sqrt{1+4\epsilon^2})-\ln 2-\sqrt{1+4\epsilon^2}+1-\frac{1}{2} \epsilon^3+\frac{1}{2} \epsilon^2\leq 0\ \forall \ \epsilon\in [0,1]$成立
令$x=\sqrt{1+4\epsilon^2}$,则$\epsilon=\frac{\sqrt{x^2-1}}{2} ,x\in [1,\sqrt{5}]$.
$\therefore g(x)=\ln(1+x)-\ln 2-\frac{\sqrt{(x^2-1)^3}}{16} +\frac{x^2-1}{8} -x+1,x\in [1,\sqrt{5}]$.
$\therefore g^{'}(x)=-\frac{3x\sqrt{x^2-1}}{16} +\frac{x}{4} +\frac{1}{x+1} -1$
$g^{''}(x)=-\frac{3}{16} (\sqrt{x^2-1}+\frac{x^2}{\sqrt{x^2-1}} )+\frac{1}{4} -\frac{1}{(x+1)^2} \leq -\frac{3x}{8} +\frac{1}{4} -\frac{1}{(x+1)^2} $
令$h(x)=\frac{3x}{8} -\frac{1}{4} +\frac{1}{(x+1)^2}$.
$h^{'}(x)=\frac{3}{8} -\frac{2}{(x+1)^3} $
$h^{''}(x)=\frac{6}{(x+1)^4}\geq 0 \ \forall \ x\in [1,\sqrt{5}]$.
$\therefore h^{'}(x)\geq h^{'}(1)=\frac{1}{8} >0$.
$\therefore h(x)\geq h(1)=\frac{3}{8} $.
$\therefore g^{'}(x)\leq g^{'}(1)=-\frac{1}{4} <0$.
$\therefore g(x)\leq g(1)=0$.
得证.

### Question 4

**Solve:**
玩家i的收益函数由以下公式给出:
$U_i(q_i,q_{-i}) = aq_i - b(q_i)^2 - c\sum_{k=1,k\neq i}^{n}q_k$

为了找到玩家i的最佳策略，我们需要找到在给定的$q_{-i}$下使$U_i(q_i,q_{-i})$最大化的$q_i$的值。取$U_i$相对于$q_i$的导数并将其设为零，我们可以得到:
$\frac{dU_i}{dq_i} = a - 2bq_i - c\sum_{k=1,k\neq i}^{n}\delta_{ik} = 0$

其中，$\delta_{ik}$是Kronecker delta函数，如果i = k，它等于1，否则等于0。

从其中求解$q_i$，我们得到:
$q_i=\frac{a-c-b\sum_{k=1,k\neq i}^{n}\delta_{ik}}{2b}$。

因此，玩家i的最佳反应是由:
$B_i(q_{-i}) = max(0,\frac{a-c-b\sum_{k=1,k\neq i}^{n}q_k}{2b})$给出.

如果方程的右边是正数，那么$q_i>0$，这是玩家i的最优策略。否则，玩家i的最优策略是根本不玩，即$q_i=0$。