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
