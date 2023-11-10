import React from "react";
import { ReactComponent as search } from './search.svg';
import { ReactComponent as tasks } from './tasks.svg';
import { ReactComponent as people } from './people.svg';
import { ReactComponent as calendar } from './calendar.svg';
import { ReactComponent as folder } from './folder.svg';

export const ICONS = {
  search,
  tasks,
  people,
  calendar,
  folder,
};

export function getIcon(key: keyof typeof ICONS, props: Record<string, any>) {
  if (!key || !ICONS[key]) {
    return React.createElement('div', null, `Иконка не найдена: ${key}`);
  }

  return React.createElement(ICONS[key], props);
}
