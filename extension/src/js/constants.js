const baseApiUrl = "http://localhost:8080";

export const headerConfig = {
    sessionKey: 'meeting-id'
}

export const responseKeys = {
    sessionKey: 'meeting_id'
}

export const apiEndpoints = {
    uploadAudio: `${baseApiUrl}/upload_audio`,
    getSuggestions: (id) => `${baseApiUrl}/suggestions/${id}`
}
