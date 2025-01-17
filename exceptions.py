class PassError(Exception):
    def catch(self, value, expression):
        self._valid = False

        if not expression:
            try:
                float(value)
            except ValueError:
                self._valid = True
            else:
                print("Response must be non-numeric.")
        else:
            try:
                float(value)
                self._valid = True
            except ValueError:
                print("Non-numeric values not accepted.")

        return self._valid
    
