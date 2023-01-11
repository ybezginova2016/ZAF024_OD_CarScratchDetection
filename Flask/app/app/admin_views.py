from app import app

@app.route('/admin/dashboard')
def admin_dashboard():
    return 'Admin dashborad'

@app.route('/admin/profile')
def admin_profile():
    return 'Admin profile'