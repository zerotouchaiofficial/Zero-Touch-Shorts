# ================================================================
# 📢 Discord Webhook Notifications — Success + Errors
# ================================================================
import os
import sys
import json
import requests
from datetime import datetime

def send_discord_notification(
    video_url,
    video_id,
    title,
    facts_count,
    video_number,
    thumbnail_set=False,
    pin_comment_set=False,
    playlist_added=False
):
    """
    Sends rich embed notification to Discord when video uploads successfully.
    """
    webhook_url = os.environ.get('DISCORD_WEBHOOK_URL')
    
    if not webhook_url:
        print('⚠️  No DISCORD_WEBHOOK_URL found - skipping notification')
        return False
    
    # Status emojis
    thumb_status = '✅ Set' if thumbnail_set else '❌ Failed'
    pin_status   = '✅ Pinned' if pin_comment_set else '⚠️ Skipped'
    play_status  = '✅ Added' if playlist_added else '⚠️ Skipped'
    
    embed = {
        "title": "🎬 New YouTube Short Uploaded!",
        "description": f"**{title}**",
        "url": video_url,
        "color": 0x00FF00,  # Green for success
        "fields": [
            {
                "name": "📊 Video Info",
                "value": (
                    f"🆔 Video ID: `{video_id}`\n"
                    f"🧠 Facts: **{facts_count}**\n"
                    f"🔢 Video Number: **#{video_number}**"
                ),
                "inline": True
            },
            {
                "name": "⚙️ Post-Upload Actions",
                "value": (
                    f"🖼️ Thumbnail: {thumb_status}\n"
                    f"📌 Comment: {pin_status}\n"
                    f"📋 Playlist: {play_status}"
                ),
                "inline": True
            },
            {
                "name": "🔗 Quick Links",
                "value": (
                    f"[▶️ Watch Short]({video_url})\n"
                    f"[📊 YouTube Studio](https://studio.youtube.com/video/{video_id}/edit)\n"
                    f"[📈 Analytics](https://studio.youtube.com/video/{video_id}/analytics)"
                ),
                "inline": False
            }
        ],
        "thumbnail": {
            "url": f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg"
        },
        "footer": {
            "text": "YouTube Shorts Bot • Automated Upload",
            "icon_url": "https://www.youtube.com/s/desktop/f506bd45/img/favicon_144x144.png"
        },
        "timestamp": datetime.utcnow().isoformat()
    }
    
    payload = {
        "username": "YouTube Shorts Bot",
        "avatar_url": "https://www.youtube.com/s/desktop/f506bd45/img/favicon_144x144.png",
        "embeds": [embed]
    }
    
    try:
        response = requests.post(
            webhook_url,
            json=payload,
            timeout=10
        )
        
        if response.status_code == 204:
            print('✅ Discord notification sent!')
            return True
        else:
            print(f'⚠️  Discord notification failed: {response.status_code}')
            print(f'   Response: {response.text}')
            return False
            
    except Exception as e:
        print(f'⚠️  Discord notification error: {e}')
        return False


def send_error_notification(error_message, video_number, stage='Unknown'):
    """
    Sends error notification to Discord when upload/generation fails.
    
    Args:
        error_message: The error text
        video_number: Which video number failed
        stage: Where it failed (e.g., 'Generation', 'Upload', 'Thumbnail')
    """
    webhook_url = os.environ.get('DISCORD_WEBHOOK_URL')
    
    if not webhook_url:
        print('⚠️  No DISCORD_WEBHOOK_URL - skipping error notification')
        return False
    
    # Truncate very long errors
    if len(error_message) > 1000:
        error_message = error_message[:997] + '...'
    
    embed = {
        "title": "❌ Upload Failed!",
        "description": f"Video **#{video_number}** failed during **{stage}**",
        "color": 0xFF0000,  # Red for errors
        "fields": [
            {
                "name": "🐛 Error Details",
                "value": f"```\n{error_message}\n```",
                "inline": False
            },
            {
                "name": "📋 What to Check",
                "value": (
                    "• GitHub Actions logs for full traceback\n"
                    "• Refresh token expiration (if invalid_grant)\n"
                    "• API quota limits (if quotaExceeded)\n"
                    "• Network/timeout issues"
                ),
                "inline": False
            }
        ],
        "footer": {
            "text": f"Video #{video_number} • Check GitHub Actions",
            "icon_url": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
        },
        "timestamp": datetime.utcnow().isoformat()
    }
    
    payload = {
        "username": "YouTube Shorts Bot",
        "avatar_url": "https://www.youtube.com/s/desktop/f506bd45/img/favicon_144x144.png",
        "embeds": [embed]
    }
    
    try:
        response = requests.post(
            webhook_url,
            json=payload,
            timeout=10
        )
        
        if response.status_code == 204:
            print('✅ Discord error notification sent!')
            return True
        else:
            print(f'⚠️  Discord error notification failed: {response.status_code}')
            return False
            
    except Exception as e:
        print(f'⚠️  Could not send Discord error: {e}')
        return False


def send_generation_start(video_number):
    """
    Optional: Notify when video generation starts.
    """
    webhook_url = os.environ.get('DISCORD_WEBHOOK_URL')
    
    if not webhook_url:
        return False
    
    payload = {
        "username": "YouTube Shorts Bot",
        "avatar_url": "https://www.youtube.com/s/desktop/f506bd45/img/favicon_144x144.png",
        "content": f"🎬 Starting generation for video **#{video_number}**..."
    }
    
    try:
        requests.post(webhook_url, json=payload, timeout=5)
        return True
    except:
        return False


# Allow running as standalone script for testing
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage:')
        print('  Success: python discord_notify.py success <url> <id> <title> <facts> <num> [thumb] [pin] [playlist]')
        print('  Error:   python discord_notify.py error <message> <num> [stage]')
        sys.exit(1)
    
    mode = sys.argv[1]
    
    if mode == 'success':
        if len(sys.argv) < 7:
            print('Error: Not enough arguments for success notification')
            sys.exit(1)
        
        success = send_discord_notification(
            video_url=sys.argv[2],
            video_id=sys.argv[3],
            title=sys.argv[4],
            facts_count=int(sys.argv[5]),
            video_number=int(sys.argv[6]),
            thumbnail_set=sys.argv[7].lower() == 'true' if len(sys.argv) > 7 else False,
            pin_comment_set=sys.argv[8].lower() == 'true' if len(sys.argv) > 8 else False,
            playlist_added=sys.argv[9].lower() == 'true' if len(sys.argv) > 9 else False
        )
        sys.exit(0 if success else 1)
        
    elif mode == 'error':
        if len(sys.argv) < 4:
            print('Error: Not enough arguments for error notification')
            sys.exit(1)
        
        success = send_error_notification(
            error_message=sys.argv[2],
            video_number=int(sys.argv[3]),
            stage=sys.argv[4] if len(sys.argv) > 4 else 'Unknown'
        )
        sys.exit(0 if success else 1)
        
    else:
        print(f'Unknown mode: {mode}')
        sys.exit(1)
