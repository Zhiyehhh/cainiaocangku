### 1.3 Mathematical models for comminication channels
#### The additive noise channel
> Gaussian noise process
> additive Gaussian noise channel
> tractability          可操作性
> predominant           占主导的

> $$
> \begin{align}
>   r(t) & = \alpha s(t) + n(t) \\
>   \alpha & \quad \text{attenuation factor} \\
>   r(t) & \quad \text{received signal} \\
>   s(t) & \quad \text{transmitted signal} \\
>   n(t) & \quad \text{additive random noise process}
> \end{align}
> $$

#### The linear filter channel
> $$
> \begin{align}
>   r(t) & = s(t) \star c(t) + n(t) \\
>   & = \int_{-\infty}^{\infty} c(\tau)\,s(t-\tau)\,\mathrm{d}\tau + n(t) \\ 
>   c(t) & \quad \text{impulse response of the linear filter} \\
>   \star & \quad \text{convolution}
> \end{align}
> $$

#### The linear time-variant filter channel
> $$
> \begin{align}
>   r(t) & = s(t) \star c(\tau ; t) + n(t) \\
>   & = \int_{-\infty}^{\infty} c(\tau ; t)\,s(t-\tau)\,\mathrm{d}\tau + n(t) \\
> & = \int_{-\infty}^{\infty} \sum_{k=1}^{L} a_k(t) \delta(\tau - \tau_k) s(t - \tau)\,\mathrm{d}\tau + n(t) \\
> & = \sum_{k=1}^{L} a_k(t) s(t - t_k) + n(t) \\
>   c(\tau ; t) & \quad \text{时变信道脉冲响应，在 $t$ 时刻观测信道，接收到 $t - \tau$ 时刻的脉冲} \\
>   L & \quad \text{多径传播} \\
>   \tau_k & \quad \text{第 $k$ 条路径的固定时延} \\
>   a_k(t) & \quad \text{时变衰减因子}
> \end{align}
> $$ 