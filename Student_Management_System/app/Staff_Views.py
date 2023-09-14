from django.shortcuts import redirect, render, HttpResponse
from .models import Staff_Notification,Staff,Staff_leave
from django.contrib import messages

def HOME(request):
    return render(request,'Staff/staff_home.html')

def NOTIFICATION(request):
    staff = Staff.objects.get(admin = request.user.id)
    
    notification = Staff_Notification.objects.filter(staff_id = staff.id)
    return render(request,'Staff/notification.html',{'notification':notification})

def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('staff_notification') 
    return None


def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.get(admin = request.user.id)
    staff_leave = Staff_leave.objects.filter(staff_id = staff)
    return render(request,'Staff/apply_leave.html',{'staff_leave':staff_leave})


def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        staff = Staff.objects.get(admin = request.user.id)
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        
        leave = Staff_leave(
            staff_id = staff,
            date = leave_date,
            message = leave_message
        )
        leave.save()
        
        
        
        messages.success(request,"Staff leave successfully send")
        return redirect('staff_apply_leave')