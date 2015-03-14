
import tempfile

import rrdtool

def get_rrd_interval(interval):
    if interval == "hourly":
        rrd_interval = "h"
    elif interval == "daily":
        rrd_interval = "d"
    elif interval == "weekly":
        rrd_interval = "w"
    elif interval == "monthly":
        rrd_interval = "m"
    elif interval == "yearly":
        rrd_interval = "y"
    else:
        raise ValueError("Unknown interval: %s" % interval)
    return rrd_interval


def subtask_site(basedir, interval, request, subtask, site):
    fd, pngpath = tempfile.mkstemp(".png")
    fname = os.path.join(basedir, request, subtask, "%s.rrd" % site)
    if not os.path.exists(fname):
        raise ValueError("No information present (request=%s, subtask=%s, site=%s)" % (request, subtask, site))
    rrdtool.graph(pngpath,
            "--imgformat", "PNG",
            "--width", "400",
            "--start", "-1%s" % get_rrd_interval(interval),
            "--vertical-label", "Jobs",
            "--lower-limit", "0",
            "--title", "%s Job Counts" % site,
            "DEF:Running=%s:Running:AVERAGE" % fname,
            "DEF:MatchingIdle=%s:MatchingIdle:AVERAGE" % fname,
            "LINE1:Running#0000FF:Running",
            "LINE2:MatchingIdle#00FF00:MatchingIdle",
            "COMMENT:%s" % site,
            "COMMENT:\\n",
            "COMMENT:            max     avg     cur\\n",
            "COMMENT:Running ",
            "GPRINT:Running:MAX:%-6.0lf",
            "GPRINT:Running:AVERAGE:%-6.0lf",
            "GPRINT:Running:LAST:%-6.0lf",
            "COMMENT:\\n",
            "COMMENT:MatchingIdle ",
            "GPRINT:MatchingIdle:MAX:%-6.0lf",
            "GPRINT:MatchingIdle:AVERAGE:%-6.0lf",
            "GPRINT:MatchingIdle:LAST:%-6.0lf\\n",
            )
    return os.fdopen(fd).read()


def subtask(basedir, interval, request, subtask):
    fd, pngpath = tempfile.mkstemp(".png")
    fname = os.path.join(basedir, request, subtask, "subtask.rrd")
    if not os.path.exists(fname):
        raise ValueError("No information present (request=%s, subtask=%s)" % (request, subtask))
    rrdtool.graph(pngpath,
            "--imgformat", "PNG",
            "--width", "400",
            "--start", "-1%s" % get_rrd_interval(interval),
            "--vertical-label", "Jobs",
            "--lower-limit", "0",
            "--title", "Subtask %s Job Counts" % subtask,
            "DEF:Running=%s:Running:AVERAGE" % fname,
            "DEF:Idle=%s:Idle:AVERAGE" % fname,
            "LINE1:Running#0000FF:Running",
            "LINE2:Idle#00FF00:Idle",
            "COMMENT:%s" % site,
            "COMMENT:\\n",
            "COMMENT:            max     avg     cur\\n",
            "COMMENT:Running ",
            "GPRINT:Running:MAX:%-6.0lf",
            "GPRINT:Running:AVERAGE:%-6.0lf",
            "GPRINT:Running:LAST:%-6.0lf",
            "COMMENT:\\n",
            "COMMENT:Idle ",
            "GPRINT:Idle:MAX:%-6.0lf",
            "GPRINT:Idle:AVERAGE:%-6.0lf",
            "GPRINT:Idle:LAST:%-6.0lf\\n",
            )
    return os.fdopen(fd).read()


def request(basedir, interval, request):
    fd, pngpath = tempfile.mkstemp(".png")
    fname = os.path.join(basedir, request, "request.rrd")
    if not os.path.exists(fname):
        raise ValueError("No information present (request=%s)" % (request, subtask))
    rrdtool.graph(pngpath,
            "--imgformat", "PNG",
            "--width", "400",
            "--start", "-1%s" % get_rrd_interval(interval),
            "--vertical-label", "Jobs",
            "--lower-limit", "0",
            "--title", "Request %s Job Counts" % request,
            "DEF:Running=%s:Running:AVERAGE" % fname,
            "DEF:Idle=%s:Idle:AVERAGE" % fname,
            "LINE1:Running#0000FF:Running",
            "LINE2:Idle#00FF00:Idle",
            "COMMENT:%s" % site,
            "COMMENT:\\n",
            "COMMENT:            max     avg     cur\\n",
            "COMMENT:Running ",
            "GPRINT:Running:MAX:%-6.0lf",
            "GPRINT:Running:AVERAGE:%-6.0lf",
            "GPRINT:Running:LAST:%-6.0lf",
            "COMMENT:\\n",
            "COMMENT:Idle ",
            "GPRINT:Idle:MAX:%-6.0lf",
            "GPRINT:Idle:AVERAGE:%-6.0lf",
            "GPRINT:Idle:LAST:%-6.0lf\\n",
            )
    return os.fdopen(fd).read()


def request_site(basedir, interval, request, site):
    fd, pngpath = tempfile.mkstemp(".png")
    fname = os.path.join(basedir, request, "%s.rrd" % site)
    if not os.path.exists(fname):
        raise ValueError("No information present (request=%s, site=%s)" % (request, site))
    rrdtool.graph(pngpath,
            "--imgformat", "PNG",
            "--width", "400",
            "--start", "-1%s" % get_rrd_interval(interval),
            "--vertical-label", "Jobs",
            "--lower-limit", "0",
            "--title", "%s Job Counts" % site,
            "DEF:Running=%s:Running:AVERAGE" % fname,
            "DEF:MatchingIdle=%s:MatchingIdle:AVERAGE" % fname,
            "LINE1:Running#0000FF:Running",
            "LINE2:MatchingIdle#00FF00:MatchingIdle",
            "COMMENT:%s" % site,
            "COMMENT:\\n",
            "COMMENT:            max     avg     cur\\n",
            "COMMENT:Running ",
            "GPRINT:Running:MAX:%-6.0lf",
            "GPRINT:Running:AVERAGE:%-6.0lf",
            "GPRINT:Running:LAST:%-6.0lf",
            "COMMENT:\\n",
            "COMMENT:MatchingIdle ",
            "GPRINT:MatchingIdle:MAX:%-6.0lf",
            "GPRINT:MatchingIdle:AVERAGE:%-6.0lf",
            "GPRINT:MatchingIdle:LAST:%-6.0lf\\n",
            )
    return os.fdopen(fd).read()

