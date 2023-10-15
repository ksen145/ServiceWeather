class Error():

    def check_error(error_code):
        if error_code == 1:
            return {'Error: ': 'API Geocode'}
        elif error_code == 2:
            return {'Error: ': 'city is None'}
        else:
            return {'Error: ': 'API weather'}
