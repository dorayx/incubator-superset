import logging

from flask_appbuilder import expose
from superset import event_logger
from superset.views.base import BaseSupersetView


class ExtendedSuperset(BaseSupersetView):
    """The base views for Extended Superset"""

    logger = logging.getLogger(__name__)

    @event_logger.log_this
    @expose("/charts/<chart_id>", methods=["GET"])
    def load_chart_component(self, chart_id=None):
        return self.render_template("superset/extended.html", chart_id=chart_id)
