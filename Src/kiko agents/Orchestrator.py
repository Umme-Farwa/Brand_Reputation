import subprocess
import time
import os

def clean_old_data():
    print(f"\n{'='*50}")
    print("🧹 Cleaning old data to fix duplication...")
    print(f"{'='*50}")

    base_path = os.path.dirname(os.path.abspath(__file__))

    files_to_delete = [

        # ✅ RAW FILE
        os.path.join(base_path, "../../data/raw/kiko_youtube_raw.csv"),

        # ✅ PROCESSED FILES
        os.path.join(base_path, "../../data/processed/kiko_final_integrated.csv"),
        os.path.join(base_path, "../../data/processed/kiko_threat_report.csv")
    ]

    for f in files_to_delete:
        if os.path.exists(f):
            try:
                os.remove(f)
                print(f"✅ Deleted: {f}")
            except Exception as e:
                print(f"⚠️ Error deleting {f}: {e}")
        else:
            print(f"ℹ️ Already clean: {f}")


def run_agent(agent_name, script_path):
    print(f"\n🚀 Running: {agent_name}...")

    try:
        subprocess.run(['python', script_path], check=True)
        return True

    except Exception as e:
        print(f"❌ Error in {agent_name}: {e}")
        return False


def main():

    print("🔔 KIKO REPUTATION SYSTEM STARTED")
    start_time = time.time()

    # ✅ CLEAN OLD DATA
    clean_old_data()

    # ✅ RUN COLLECTOR FIRST
    if run_agent("Collector Agent", "kiko_collector_agent.py"):

        # ✅ RUN PARSER
        if run_agent("Parser Agent", "kiko_parser_agent.py"):

            # ✅ RUN THREAT DETECTOR
            if run_agent("Threat Detector", "kiko_threat_detector.py"):

                # ✅ VALIDATION
                run_agent("Validation Metrics", "kiko_validation_agent.py")

                # ✅ REPORTER
                run_agent("Reporter Agent", "kiko_reporter_agent.py")

    duration = round(time.time() - start_time, 2)

    print(f"\n🎉 DONE! Pipeline completed in {duration}s")


if __name__ == "__main__":
    main()
