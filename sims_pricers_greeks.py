# Monte Carlo Simulator
def MC(batches,St,K,r,q,sigma,T,flavor='Call',alpha=0,style='euro',seed=2,t=0):
    dt = T-t
    mu = r - q - sigma*sigma*0.5*dt
    
    d1 = ((np.log(St/K) + (r - q)*(dt)) / sigma*np.sqrt(dt)) + 0.5*sigma*np.sqrt(dt)
    d2 = ((np.log(St/K) + (r - q)*(dt)) / sigma*np.sqrt(dt)) - 0.5*sigma*np.sqrt(dt)
    price = []
    stdev = []
    
    for n in batches:
        np.random.seed(seed)
        draws = np.random.normal(size=n)
        stoch = sigma*np.sqrt(dt)*draws
        ST = St*np.exp(mu + stoch)
        
        if flavor == 'Put':
            payoff = np.maximum((K - ST),0)
        elif flavor == 'Call':
            payoff = np.maximum((ST - K),0)
        elif flavor == 'Asymptotic Call':
            payoff = np.maximum((K - K*K/ST),0)
        elif flavor == 'Control Variate':
            payoff = (K/ST - alpha)* np.maximum((ST - K),0)
        elif flavor == 'Control Variate2':
            payoff = (K/ST - alpha)* np.maximum((ST - K),0) + St*np.exp(-q*dt)*norm.cdf(d1) - K*np.exp(-r*dt)*norm.cdf(d2)
        elif flavor == 'Power Call':
            payoff = np.maximum((ST*ST - K),0)
        else:
            payoff = ST
       
        PVs = np.exp(-r*dt)*payoff 
        price.append(np.mean(PVs))
        stdev.append(np.std(PVs)/np.sqrt(n))
        #print(ST)
    return price, stdev

# Lookback Option Monte Carlo Function
def lookback_MC(batches, freqs, S,K,r,q,sigma,T,flavor='c',style='float',display='no',t=0,antithetic='no'):
    '''This function generate batches of n normally distributed random variables, which are used to generate 
    a geometric brownian motion along m sample paths.  Then we calculate the maximum values, for each batch, along
    each m paths for the specified frequency of m.  We end up with a row vector of n maximums, which are then
    used to calculate the payoff.  We take the mean of each of these, and discount to the present value.'''
    num_steps = 252
    dt = T/num_steps
    
    ST = np.zeros((num_steps+1,batches))
    
    
    Smax = []
    Smin = []
    ST[0,:] = S
    
    
    
    payout = np.zeros(num_steps)
    payoutLookback = []
    lookbackMean = []
    lookbackVariance = []
    PV = []
    if antithetic == 'yes':
        batches = batches//2
        for i in range(0,num_steps):
        
            mu = (r - q - sigma*sigma*0.5)*dt
            draws = np.random.normal(size=batches)
            stoch = sigma*np.sqrt(dt)*draws
            stoch = np.concatenate((stoch, -stoch)) 
       
            ST[i+1,:] = ST[i,:]*np.exp(mu + stoch)
            
            payout[i] = np.average(np.maximum((ST[i,:] - K),0))
    else:
        for i in range(0,num_steps):   
            mu = (r - q - sigma*sigma*0.5)*dt
            draws = np.random.normal(size=batches)
            stoch = sigma*np.sqrt(dt)*draws
            
            ST[i+1,:] = ST[i,:]*np.exp(mu + stoch)
            
            
            payout[i] = np.average(np.maximum((ST[i,:] - K),0))
    
    for m in freqs:
        Smax.append(np.max(ST[int(num_steps/m)-1:num_steps:int(num_steps/m)],0))
        Smin.append(np.min(ST[int(num_steps/m)-1:num_steps:int(num_steps/m)],0))

    for i in range(0,num_steps):
        PV.append(np.exp(-r*T)*payout[i])
    for i in range(0,len(freqs)):
        if antithetic=='yes':
            payouts = np.maximum((Smax[i]-K),0)
            avg_payouts = np.average([payouts[0:batches],payouts[batches:]],axis=0)
            payoutLookback.append(np.exp(-r*T)*avg_payouts)
        else:
            payoutLookback.append(np.exp(-r*T)*np.maximum((Smax[i] - K),0))
        lookbackVariance.append(np.std(payoutLookback[i]))
        lookbackMean.append(np.mean(payoutLookback[i]))
   
    return lookbackMean,lookbackVariance/np.sqrt(batches)

# Closed-Form Lookback Function
def lookback_Analytic(S,K,r,q,sigma,T,flavor = 'fixed strike call',t=0):
    dt = T-t
    d1 = ((np.log(S/K) + (r - q)*(dt)) / sigma*np.sqrt(dt)) + 0.5*sigma*np.sqrt(dt)
    d2 = ((np.log(S/K) + (r - q)*(dt)) / sigma*np.sqrt(dt)) - 0.5*sigma*np.sqrt(dt)
    d1_ = ((np.log(S/K) - (r - q)*(dt)) / sigma*np.sqrt(dt)) - 0.5*sigma*np.sqrt(dt)
    d2_ = ((np.log(S/K) - (r - q)*(dt)) / sigma*np.sqrt(dt)) + 0.5*sigma*np.sqrt(dt)
    
    euro_call = S*np.exp(-q*dt)*norm.cdf(d1) - K*np.exp(-r*dt)*norm.cdf(d2)
    euro_put = K*np.exp(-r*dt)*norm.cdf(d2_) - S*np.exp(-q*dt)*norm.cdf(d1_)
    
    lookback1 = np.exp(-r*dt)*(sigma*sigma/(2*r))*S
    lookback_c = (np.exp(r*dt)*norm.cdf(d1) - (np.power((S/K),(-(2*r)/(sigma*sigma))))*norm.cdf(d1-(((2*r)/(sigma))*np.sqrt(dt))))
    lookback_p = (np.power((S/K),(-(2*r)/(sigma*sigma))))*norm.cdf(-d1+(((2*r)/(sigma))*np.sqrt(dt)))-(np.exp(r*dt)*norm.cdf(-d1))
    
    if flavor == 'fixed strike call':
        price =  euro_call + lookback1*lookback_c
    if flavor == 'fixed strike put':
        price = euro_put + lookback1*(lookback_p)
    
    
    return price    


# Black-Scholes European Pricer
def BS(S,K,r,q,sigma,T,flavor='c',style='euro',display='no',t=0):
    dt = T-t
    d1 = ((np.log(S/K) + (r - q)*(dt)) / sigma*np.sqrt(dt)) + 0.5*sigma*np.sqrt(dt)
    d2 = ((np.log(S/K) + (r - q)*(dt)) / sigma*np.sqrt(dt)) - 0.5*sigma*np.sqrt(dt)
    d1_ = ((np.log(S/K) - (r - q)*(dt)) / sigma*np.sqrt(dt)) - 0.5*sigma*np.sqrt(dt)
    d2_ = ((np.log(S/K) - (r - q)*(dt)) / sigma*np.sqrt(dt)) + 0.5*sigma*np.sqrt(dt)
    if flavor == 'c':
        price = S*np.exp(-q*dt)*norm.cdf(d1) - K*np.exp(-r*dt)*norm.cdf(d2)
        delta = np.exp(-q*dt)*norm.cdf(d1)
        gamma = np.exp(-q*dt)*(1/(S*sigma*np.sqrt(dt)))*norm.pdf(d1)
        vega = S*np.exp(-q*dt)*np.sqrt(dt)*norm.pdf(d1)
        theta = -S*sigma*np.exp(-q*dt)*(1/(2*np.sqrt(dt)))*norm.pdf(d1) +q*S*np.exp(-q*dt)*norm.cdf(d1) - r*K*np.exp(-r*dt)*norm.cdf(d2)
        rho_q = -dt*S*np.exp(-q*T)*norm.cdf(d1)
    if flavor == 'p':
        price = K*np.exp(-r*dt)*norm.cdf(d2_) - S*np.exp(-q*dt)*norm.cdf(d1_)
        delta = -np.exp(-q*dt)*norm.cdf(d1_)
        gamma = np.exp(-q*dt)*(1/(S*sigma*np.sqrt(dt)))*norm.pdf(d1)
        vega = S*np.exp(-q*dt)*np.sqrt(dt)*norm.pdf(d1)
        theta = -S*sigma*np.exp(-q*dt)*(1/(2*np.sqrt(dt)))*norm.pdf(d1) -q*S*np.exp(-q*dt)*norm.cdf(d1_) + r*K*np.exp(-r*dt)*norm.cdf(d2_)
    if display == "yes":
        print("Price: {:.4f}".format(price))
        print("Delta: {:.4f}".format(delta))
        print("Gamma: {:.4f}".format(gamma))
        print("Vega: {:.4f}".format(vega))
        print("Theta: {:.4f}".format(theta))

    return price, delta, gamma, vega, theta, rho_q

# greeks simulation
def MC_greeks(batches,St,K,r,q,sigma,T,flavor='Call',alpha=0,style='euro',seed=2,t=0):
    dt = T-t
    d2s = []
    rho = []
    for i in range(len(So)):
        
    for n in batches:
        np.random.seed(seed)
        draws = np.random.normal(size=n)
        stoch = sigma*np.sqrt(dt)*draws
        
        mu = (r - q - sigma*sigma*0.5*dt)
        ST = (St*np.exp(mu + stoch))
        

        if flavor == 'Put':
            payoff = np.maximum((K - ST),0)
        elif flavor == 'Call':
            payoff = np.maximum((ST - K),0)
        elif flavor == 'Asymptotic Call':
            payoff = np.maximum((K - K*K/ST),0)
        elif flavor == 'Control Variate':
            payoff = (K/ST - alpha)* np.maximum((ST - K),0)
        elif flavor == 'Control Variate2':
            payoff = (K/ST - alpha)* np.maximum((ST - K),0) + St*np.exp(-q*dt)*norm.cdf(d1) - K*np.exp(-r*dt)*norm.cdf(d2)
        elif flavor == 'Power Call':
            payoff = np.maximum((ST*ST - K),0)
    
    return payoff, rho
