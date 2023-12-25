from .models import Incidents,Handlers
from .common import WorkStatus

def get_available_handlers():
    if available_handler := Handlers.objects.filter(assignment_count=0):
        for h in available_handler:
            if incident := Incidents.objects.filter(status=WorkStatus.PENDING
                        ).order_by('severity','-timestamp').first():
                incident.assigned_to = h.name
                incident.status = WorkStatus.WORKING
                incident.save()
    
    return True


while True:
    get_available_handlers()
    