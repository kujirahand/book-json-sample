export interface BBSLogs {
    id:       string;
    title:    string;
    date:     string;
    priority: Priority;
    status:   Status;
    link:     string;
}

export enum Priority {
    中 = "中",
    低 = "低",
    緊急 = "緊急",
    高 = "高",
}

export enum Status {
    アイデア = "アイデア",
    修正中 = "修正中",
    再修正依頼 = "再修正依頼",
    告知 = "告知",
    感想 = "感想",
    感謝 = "感謝",
    未処理 = "未処理",
    確認待ち = "確認待ち",
    解決 = "解決",
    詳細求む = "詳細求む!",
    調査中 = "調査中",
    議論中 = "議論中",
    重複 = "重複",
}
