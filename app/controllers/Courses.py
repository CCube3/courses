from system.core.controller import *
# from system.core.router import routes
# routes['default_controller'] = 'Courses'
# routes['POST']['/courses/add'] = 'Courses#add'
# routes['GET']['/courses/destroy/<int:course_id>'] = 'Courses#remove'
# routes['POST']['/courses/delete/<int:course_id>'] = 'Courses#delete'
class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        # Note that we have to load the model before using it
        self.load_model('Course')

    def index(self):
        session['data'] = self.models['Course'].get_all_courses()
        return self.load_view('index.html')

    # This is how a method with a route parameter that provides the id would work
    # We would set up a GET route for this method
    def remove(self, course_id):
        # Note how we access the model using self.models
        course = self.models['Course'].get_course_by_id(course_id)
        return self.load_view('remove.html', course=course)

    # This is how a method used to add a course would look
    # We would set up a POST route for this method
    def add(self):
        # in actuality, data for the new course would come
        # from a form on our client
        if len(request.form['name']) < 15:
            flash('Course name must be at least 15 characters long!')
        elif not ['name']:
            flash('Name cannot be blank', 'name')
            return redirect('/')
        course_details = {
            'title': request.form['name'],
            'description': request.form['description']
        }
        self.models['Course'].add_course(course_details)
        return redirect('/')

    # This is how a method used to update a course would look
    # We would set up a POST route for this method
    def update(self, course_id):
        # in actuality, data for updating the course would come
        # from a form on our client
        course_details = {
            'id': course_id,
            'title': 'Python 2.0',
            'description': 'This course is unreal!'
        }
        self.models['Course'].update_course(course_details)
        return redirect('/')

     # This is how a method used to delete a course would look
     # We would set up a POST route for this method
    def delete(self, course_id):
        self.models['Course'].delete_course(course_id)
        return redirect('/')
