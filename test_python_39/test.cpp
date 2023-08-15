#include <thread>
#include <cstdlib>

void RunScript() {
    system("RUN.bat");
}

int main() {
    std::thread test_thread(RunScript);

    std::this_thread::sleep_for(std::chrono::seconds(60));

    if (test_thread.joinable()) {
        return EXIT_SUCCESS;
    } else {
        return EXIT_FAILURE;
    }
}
