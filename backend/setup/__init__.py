import glob
import importlib
import logging
import os
from os.path import dirname, join, basename, isfile

from django.http import HttpResponseForbidden, HttpResponse


def run_items():
    files = sorted(glob.glob(join(dirname(__file__), "*.py")))
    modules = [basename(f)[:-3] for f in files if isfile(f) and not f.endswith('__init__.py')]

    for module in modules:
        try:
            logging.info("Running setup module: {}".format(module))
            command_module = importlib.import_module("infotrem.setup.{}".format(module))
            command_module.run()
        except ImportError:
            # Display error message
            logging.error("Unable to import module: {}".format(module))


def run_from_request(request):
    if 'pass' not in request.GET or request.GET['pass'] != os.environ['SETUP_PASS']:
        return HttpResponseForbidden("Wrong password")

    run_items()

    return HttpResponse("Setup complete")
