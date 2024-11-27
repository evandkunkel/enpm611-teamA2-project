import config
from data_loader import DataLoader
from model import Issue,Event
from typing import List
from datetime import datetime
from plotting import plot_gantt_chart

class IssueLifecycleAnalysis:
    
    def __init__(self):
        self.USER:str = config.get_parameter('user')
        self.FEATURE:str = config.get_parameter('feature')
    
    def run(self):
        issues_list:List[Issue] = DataLoader().get_issues()
        
        reopened_events:int = 0
        
        reopened_issues_list: List[Issue] = []
        
        gantt_data = []
        
        
        for i in issues_list:
            for e in i.events:
                if e.event_type == 'reopened':
                    reopened_issues_list.append(i)
        
        j=1            
        for i in reopened_issues_list:
            lifecycle = {
                "issue_number": j,
                "issue_id": i.number,
                "created_date": i.created_date,
                "updated_date": i.updated_date,
                "closed_dates": [],
                "reopened_dates": [],
            }
            
            for e in i.events:
                if e.event_type == "reopened":
                    lifecycle["reopened_dates"].append(e.event_date)
                if e.event_type == "closed":
                    lifecycle["closed_dates"].append(e.event_date)
                    
            gantt_data.append(lifecycle)
            j+=1
        
        plot_gantt_chart(gantt_data)
    
  
        

if __name__ == '__main__':
    IssueLifecycleAnalysis().run()