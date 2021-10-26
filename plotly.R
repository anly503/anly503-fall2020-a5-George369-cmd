library(ggplot2)
library(plotly)
sums <- read.csv("sums.csv")
fig <- plot_ly(sums, x = ~date, y = ~sum,
               color = ~category,
               type='scatter', mode='lines',
               hovertemplate=paste('<b>',sums$category,'</b><br>Date=%{x}<br>Sum=%{y:.2f}')) %>% 
  plotly::layout(xaxis=list(title='Date'),
                 yaxis=list(title='Summation'),
                 title = 'Total Expenditure of Energy',
                 showlegend=FALSE)
fig