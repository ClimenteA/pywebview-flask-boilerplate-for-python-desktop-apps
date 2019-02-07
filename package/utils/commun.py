import os
import json
import string
import random
import shutil
import ntpath
import time
import traceback
from time import mktime
from datetime import timedelta
from datetime import datetime
import xlwings as xw



class Commun:
    """Commun unspecific funcs """

    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    numbers = list(string.digits)
    punctuation_marks = list(str(string.punctuation))

    characters_list = upper + lower + numbers
    

    def read_json(self, filepath):
        """Return a dict form a json file"""
        with open(filepath) as j:
            adict = json.load(j)
        return adict

    def write_json(self, thedict, thepath, fname=None):
        """Write dict to Json file"""
        if fname != None:
            thepath = os.path.join(thepath, fname)

        with open(thepath, "w") as f:
            #Write to file
            json.dump(thedict, f)
    
    def config_info(self):
        """Get as a dict the config.json file"""
        info_dict = self.read_json('config.json')
        return info_dict


    def generate_id(self, len_id):
        """Generate a random series of chars upper/lower + numbers"""
        custom_id = []
        for _ in range(len_id):
            custom_id.append(random.choice(self.characters_list))
        custom_id_result = ''.join(custom_id)
        return custom_id_result


    def current_date(self, date_format='%Y-%m-%d'):
        """Get current date in year-month-day format(default)"""
        date = datetime.now().strftime(date_format)
        return date


    def wait_file_on_disk(self, save_path_file, timeout=900):
        """Wait file to be saved in the path specified on disk"""
        wait_until = datetime.now() + timedelta(seconds=timeout)
        while os.path.isfile(save_path_file) != True:
            if wait_until < datetime.now():
                raise ValueError("Timeout reached!")
            time.sleep(1)

    def copy_file(self, src, dst):
        """Copy file from source to destination"""
        shutil.copy2(src, dst)

    def copy_dirs(self, src, dst, symlinks=False, ignore=None):
        """Copy dirs and it's items from src to dst"""
        if not os.path.exists(dst):
            os.makedirs(dst)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                self.copy_dirs(s, d, symlinks, ignore)
            else:
                if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                    shutil.copy2(s, d)

    def delete_dirs(self, apath):
        """Delete directory and all it's subfolders"""
        try:
            shutil.rmtree(apath) #delete folders, subfolders and files
        except:
            shutil.rmtree(apath, ignore_errors=True) #delete files that are not opened
            raise Exception("Not all files were deleted from {}".format(apath))

    def move_folder(self, src, dst):
        """Rename/move file or directory"""
        shutil.move(src, dst)
    
    def folder_exists(self, folder_path):
        """Check if directory exists in specified path"""
        return os.path.isdir(folder_path)
           
    
    def file_exists(self, file_path):
        """Check if file exists in specified path"""
        return os.path.isfile(file_path)

    def get_file_name(self, apath):
        """Get the file name from a given path"""
        fname = ntpath.basename(apath)
        return fname

    def accept_only_files(self, apath):
        """Raise error if a dir is found in the path specified"""
        files = os.listdir(apath)
        for f in files:
            file_path = os.path.join(apath, f)
            if not self.file_exists(file_path):
                raise Exception("Only files are accepted! Remove: {}".format(file_path))

    def listify_string(self, astring, delimiter=','):
        """Make a list from a string spliting it by it's delimiter"""
        strListifyed = astring.split(delimiter)
        astringListifyed = [s.strip() for s in strListifyed]
        return astringListifyed


    def get_files(self, root_path):
        """Walk thru a start path and return a list of paths to files"""

        allfiles = []
        for root, _, files in os.walk(root_path):
            for f in files:
                path_tofile = os.path.join(root, f)
                allfiles.append(path_tofile)
        
        return allfiles

    
    def get_folders(self, apath):
        """List folders from a given path"""
        files = os.listdir(apath)
        folders_paths = []
        for f in files:
            folder_path = os.path.join(apath, f)
            if os.path.isdir(folder_path):
                folders_paths.append(folder_path)

        return folders_paths


    def list_duplicates(self, seq):
        """Check for duplicates"""
        seen = set()
        seen_add = seen.add
        # adds all elements it doesn't know yet to seen and all other to seen_twice
        seen_twice = set( x for x in seq if x in seen or seen_add(x) )
        # turn the set into a list (as requested)
        return list(seen_twice)


    def get_unique_list(self, seq):
        """Get a uniques list but peserve order"""
        seen = set()
        seen_add = seen.add
        return [x for x in seq if not (x in seen or seen_add(x))]


    def remove_null(self, data):
        """Remove empty strings or None values from lists and dicts"""
        if isinstance(data, dict):
            clean_data = {}
            for k, v in data.items():
                if v == "" or len(v) == 0 or v == None:
                    pass
                else:
                    clean_data[k] = v
            return clean_data
        
        elif isinstance(data, list):
            clean_data = []
            for v in data:
                if v == "" or len(v) == 0 or v == None:
                    pass
                else:
                    clean_data.append(v)
            return clean_data
        else:
            raise Exception("Only simple dict and list types are accepted!")


    def remove_punctuation(self, astring):
        """Remove punctuation marks from string to avoid sql issues"""
        newstr = []
        for c in astring:
            if c not in self.punctuation_marks:
                newstr.append(c)
        return "".join(newstr)
    
    
    def get_file_size_mtime(self, filepath):
        """Get file size in bytes and modification date"""
        metadata = os.stat(filepath)
        file_size = metadata.st_size # bytes
        filetime = time.localtime(metadata.st_mtime)
        dt = datetime.fromtimestamp(mktime(filetime))
        creation_date = dt.strftime('%Y-%m-%d')

        fileinfodict = {'FileSize':file_size,
                        'ModificationDate': creation_date
                        }

        return fileinfodict


    def xl_look(self, xlfilepath, colsrange, close=False):
        """Change the look of the excel"""
        import pythoncom
        pythoncom.CoInitialize() 

        xl = xw.Book(xlfilepath)
        sht = xl.sheets[0]
        sht.range(colsrange).columns.autofit()
        sht.range(colsrange).color = (51,153,255)# blue
        xl.save()
        if close:
            xl.close()
        
    def show_excel(self, xlfilepath):
        xl = xw.Book(xlfilepath)


    def write_traceback(self, err):
        """Write the error on a error txt file show the traceback of the error"""
        err_time = str(datetime.now()) #'2011-05-03 17:45:35.177000'
        tb_error_msg = traceback.format_exc()
        errormessage = "###########\n{}\nERROR:\n{}\n\nDetails:\n{}\n###########\n\n\n".format(err_time, err, tb_error_msg)
        
        with open("ERRORS.txt", "a") as errfile:
            errfile.write(errormessage)
        
        return errormessage


    # def send_mail(self, TO_MAIL, SUBJECT_MAIL, MESSAGE_MAIL, FROM_MAIL="", FROM_PASSWORD=""):
    #     """Send email using Flask-mail module"""
    #     from flask import Flask
    #     from flask_mail import Mail, Message

    #     app = Flask(__name__)
    #     conf = self.read_json("config.json")

    #     if FROM_MAIL == "":
    #         FROM_MAIL = conf["MAIL_USERNAME"]
    #     if FROM_PASSWORD == "":
    #         FROM_PASSWORD = conf["MAIL_PASSWORD"]

    #     app.config['MAIL_SERVER'] = conf["MAIL_SERVER"]
    #     app.config['MAIL_PORT'] = conf["MAIL_PORT"]
    #     app.config['MAIL_USERNAME'] = FROM_MAIL
    #     app.config['MAIL_PASSWORD'] = FROM_PASSWORD
    #     app.config['MAIL_USE_TLS'] = bool(conf["MAIL_PORT"])
    #     app.config['MAIL_USE_SSL'] = bool(conf["MAIL_PORT"])

    #     mail = Mail(app)

    #     if isinstance(TO_MAIL, str):
    #         TO_MAIL = [TO_MAIL]

    #     msg = Message(SUBJECT_MAIL, sender=conf["MAIL_USERNAME"], recipients=TO_MAIL)
    #     msg.body = MESSAGE_MAIL
    #     mail.send(msg)
 


