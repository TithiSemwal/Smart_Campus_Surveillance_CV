def detect_crowd(detections):
    if len(detections) >= 4:
        return "Alert: Crowd Forming"
    return None